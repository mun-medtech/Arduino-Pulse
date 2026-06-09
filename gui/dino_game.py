import sys
import math
import random
import glob
import threading
from collections import deque

import pygame

def list_ports():
    if sys.platform.startswith("win"):
        return [f"COM{i}" for i in range(1, 21)]
    return sorted(glob.glob("/dev/ttyACM*") + glob.glob("/dev/ttyUSB*"))


class SerialReader(threading.Thread):
    SPIKE_THRESHOLD = 200
    HISTORY = 8

    def __init__(self, port, baud=9600):
        super().__init__(daemon=True)
        self.port = port
        self.baud = baud
        self._running = True
        self.value = 0.0
        self.spike = False
        self._history = deque([0.0] * self.HISTORY, maxlen=self.HISTORY)
        self.error: str | None = None

    def run(self):
        try:
            import serial
            ser = serial.Serial(self.port, self.baud, timeout=1)
            while self._running:
                line = ser.readline().decode("utf-8", errors="replace").strip()
                if line:
                    try:
                        raw = float(line)
                        prev_avg = sum(self._history) / len(self._history)
                        self._history.append(raw)
                        self.value = raw
                        if raw - prev_avg > self.SPIKE_THRESHOLD:
                            self.spike = True
                    except ValueError:
                        pass
            ser.close()
        except Exception as e:
            self.error = str(e)

    def consume_spike(self) -> bool:
        if self.spike:
            self.spike = False
            return True
        return False

    def stop(self):
        self._running = False

BG = (15,  17,  23)
GROUND = (40,  44,  55)
ACCENT = (0,  230, 130)
OBSTACLE = (220, 70,  70)
PLAYER_C = (0,  200, 255)
TEXT_C = (180, 190, 210)
DIM = (60,  65,  80)
GRAPH_C = (0,  180, 100)
SPIKE_C = (255, 200,  50)

W, H = 900, 420
FPS = 60
GROUND_Y = H - 90

class Player:
    W, H_   = 36, 44
    JUMP_V  = -15
    GRAVITY = 0.7

    def __init__(self):
        self.x   = 110
        self.y   = float(GROUND_Y - self.H_)
        self.vy  = 0.0
        self.on_ground = True
        self.dead = False
        self.flash = 0
        
    def jump(self):
        if self.on_ground:
            self.vy = self.JUMP_V

    def update(self):
        self.vy += self.GRAVITY
        self.y  += self.vy
        if self.y >= GROUND_Y - self.H_:
            self.y  = float(GROUND_Y - self.H_)
            self.vy = 0.0
            self.on_ground = True
        else:
            self.on_ground = False
        if self.flash > 0:
            self.flash -= 1

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.W, self.H_)

    def draw(self, surf, t):
        r = self.rect()
        color = (255, 80, 80) if self.flash > 0 else PLAYER_C

        pygame.draw.rect(surf, color, r, border_radius=6)

        visor = pygame.Rect(r.x + 6, r.y + 8, 18, 10)
        pygame.draw.rect(surf, BG, visor, border_radius=3)
        pygame.draw.rect(surf, ACCENT, visor, 1, border_radius=3)

        leg_off = int(math.sin(t * 0.25) * 6) if self.on_ground else 0
        pygame.draw.rect(surf, color, (r.x + 6,  r.bottom, 8, 8 + leg_off))
        pygame.draw.rect(surf, color, (r.x + 22, r.bottom, 8, 8 - leg_off))

class Obstacle:
    TYPES = [
        {"w": 22, "h": 48},
        {"w": 16, "h": 64},
        {"w": 36, "h": 36},
    ]

    def __init__(self, speed):
        t = random.choice(self.TYPES)
        self.w = t["w"]
        self.h = t["h"]
        self.x = float(W + 20)
        self.y = GROUND_Y - self.h
        self.speed = speed

    def update(self):
        self.x -= self.speed

    def rect(self):
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)

    def draw(self, surf):
        r = self.rect()
        pygame.draw.rect(surf, OBSTACLE, r, border_radius=4)
        # highlight edge
        pygame.draw.rect(surf, (240, 110, 110), r, 2, border_radius=4)

    def off_screen(self):
        return self.x + self.w < 0

class MiniGraph:
    W, H_ = 200, 50
    MAX   = 1023

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.buf = deque([0.0] * self.W, maxlen=self.W)
        self.surf = pygame.Surface((self.W, self.H_), pygame.SRCALPHA)

    def push(self, v):
        self.buf.append(v)

    def draw(self, screen, spike_now):
        self.surf.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surf, (25, 28, 38, 200), (0, 0, self.W, self.H_))
        pygame.draw.rect(self.surf, DIM, (0, 0, self.W, self.H_), 1)

        pts = list(self.buf)
        for i in range(1, len(pts)):
            x1, x2 = i - 1, i
            y1 = int(self.H_ - pts[i-1] / self.MAX * (self.H_ - 4) - 2)
            y2 = int(self.H_ - pts[i]   / self.MAX * (self.H_ - 4) - 2)
            c  = SPIKE_C if spike_now and i == len(pts) - 1 else GRAPH_C
            pygame.draw.line(self.surf, c, (x1, y1), (x2, y2), 1)

        screen.blit(self.surf, (self.x, self.y))


class Cloud:
    def __init__(self):
        self.reset(spawn=True)

    def reset(self, spawn=False):
        self.x = W + random.randint(0, 200) if not spawn else random.randint(0, W)
        self.y = random.randint(30, 120)
        self.w = random.randint(60, 130)
        self.speed = random.uniform(0.4, 1.0)
        self.alpha = random.randint(20, 50)

    def update(self):
        self.x -= self.speed
        if self.x + self.w < 0:
            self.reset()

    def draw(self, surf):
        s = pygame.Surface((self.w, 22), pygame.SRCALPHA)
        pygame.draw.ellipse(s, (*DIM, self.alpha), (0, 0, self.w, 22))
        surf.blit(s, (int(self.x), self.y))


def port_select_screen(screen, clock, font, small_font):
    ports = list_ports()
    bauds = ["9600", "19200", "57600", "115200"]
    sel_port = 0
    sel_baud = 0
    mode = "port"

    while True:
        screen.fill(BG)

        title = font.render("SERIAL JUMP", True, ACCENT)
        screen.blit(title, (W // 2 - title.get_width() // 2, 80))

        sub = small_font.render("Select port & baud to play  ·  SPACE to demo (no serial)", True, DIM)
        screen.blit(sub, (W // 2 - sub.get_width() // 2, 130))

        # Port list
        plbl = small_font.render("PORT", True, ACCENT if mode == "port" else DIM)
        screen.blit(plbl, (W // 2 - 140, 185))
        for i, p in enumerate(ports or ["No ports found"]):
            c = ACCENT if i == sel_port and mode == "port" else TEXT_C if i == sel_port else DIM
            t = small_font.render(("▶ " if i == sel_port else "  ") + p, True, c)
            screen.blit(t, (W // 2 - 130, 210 + i * 26))

        # Baud list
        blbl = small_font.render("BAUD", True, ACCENT if mode == "baud" else DIM)
        screen.blit(blbl, (W // 2 + 60, 185))
        for i, b in enumerate(bauds):
            c = ACCENT if i == sel_baud and mode == "baud" else TEXT_C if i == sel_baud else DIM
            t = small_font.render(("▶ " if i == sel_baud else "  ") + b, True, c)
            screen.blit(t, (W // 2 + 70, 210 + i * 26))

        hint = small_font.render("←→ switch column   ↑↓ select   ENTER connect   SPACE demo", True, DIM)
        screen.blit(hint, (W // 2 - hint.get_width() // 2, H - 50))

        pygame.display.flip()
        clock.tick(30)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:   mode = "port"
                if e.key == pygame.K_RIGHT:  mode = "baud"
                if e.key == pygame.K_UP:
                    if mode == "port" and ports: sel_port = (sel_port - 1) % len(ports)
                    if mode == "baud":            sel_baud = (sel_baud - 1) % len(bauds)
                if e.key == pygame.K_DOWN:
                    if mode == "port" and ports: sel_port = (sel_port + 1) % len(ports)
                    if mode == "baud":            sel_baud = (sel_baud + 1) % len(bauds)
                if e.key == pygame.K_RETURN and ports:
                    return ports[sel_port], int(bauds[sel_baud])
                if e.key == pygame.K_SPACE:
                    return None, None   #demo mode


def game(screen, clock, font, small_font, serial: SerialReader | None):
    player = Player()
    obstacles = []
    clouds = [Cloud() for _ in range(6)]
    graph = MiniGraph(W - 220, 10)

    speed = 5.0
    score = 0
    best = 0
    t = 0
    spawn_t = 0
    spawn_gap = 90
    running = True
    started = False
    demo_t = 0

    def reset():
        nonlocal player, obstacles, speed, score, t, spawn_t, spawn_gap, started
        player = Player()
        obstacles = []
        speed = 5.0
        score = 0
        t = 0
        spawn_t = 0
        spawn_gap = 90
        started = False

    while running:
        dt = clock.tick(FPS)
        t += 1
        spike_now = False

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "quit"
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    return "menu"
                if e.key == pygame.K_SPACE:
                    if player.dead:
                        best = max(best, score)
                        reset()
                    else:
                        started = True
                        player.jump()

        if serial:
            v = serial.value
            graph.push(v)
            if serial.consume_spike():
                spike_now = True
                if player.dead:
                    best = max(best, score)
                    reset()
                else:
                    started = True
                    player.jump()
        else:
            demo_t += 1
            fake_v = 512 + 400 * math.sin(demo_t * 0.04)
            graph.push(fake_v)
            if demo_t % 180 == 0:
                spike_now = True
                if not player.dead:
                    started = True
                    player.jump()

        if started and not player.dead:
            score  += 1
            speed   = 5.0 + score * 0.003
            spawn_t += 1

            player.update()

            if spawn_t >= spawn_gap:
                obstacles.append(Obstacle(speed))
                spawn_t   = 0
                spawn_gap = random.randint(55, 110)

            for ob in obstacles:
                ob.speed = speed
                ob.update()
            obstacles = [o for o in obstacles if not o.off_screen()]

            for ob in obstacles:
                if player.rect().inflate(-8, -8).colliderect(ob.rect()):
                    player.dead  = True
                    player.flash = 20
                    best = max(best, score)

        for c in clouds:
            c.update()

        screen.fill(BG)

        for c in clouds:
            c.draw(screen)

        pygame.draw.rect(screen, GROUND, (0, GROUND_Y, W, 4))
        pygame.draw.rect(screen, DIM,    (0, GROUND_Y + 4, W, 2))

        for i in range(0, W, 40):
            dash_x = (i - t * int(speed)) % W
            pygame.draw.rect(screen, DIM, (dash_x, GROUND_Y + 10, 20, 2))

        for ob in obstacles:
            ob.draw(screen)

        player.draw(screen, t)

        sc_txt = font.render(f"{score:05d}", True, TEXT_C)
        screen.blit(sc_txt, (W - sc_txt.get_width() - 20, 14))
        if best:
            hi = small_font.render(f"BEST {best:05d}", True, DIM)
            screen.blit(hi, (W - hi.get_width() - 20, 46))

        graph.draw(screen, spike_now)
        glbl = small_font.render("ANALOG IN", True, DIM)
        screen.blit(glbl, (W - 220, 64))

        if serial and serial.error:
            err = small_font.render(f"⚠ {serial.error}", True, OBSTACLE)
            screen.blit(err, (10, 10))
        elif serial:
            dot_c = SPIKE_C if spike_now else ACCENT
            pygame.draw.circle(screen, dot_c, (14, 18), 5)
            lbl = small_font.render(f"{serial.value:.0f}", True, dot_c)
            screen.blit(lbl, (24, 11))
        else:
            demo_lbl = small_font.render("DEMO MODE  ·  ESC = menu", True, DIM)
            screen.blit(demo_lbl, (10, 10))

        if spike_now:
            flash = pygame.Surface((W, H), pygame.SRCALPHA)
            flash.fill((255, 220, 50, 18))
            screen.blit(flash, (0, 0))

        if player.dead:
            ov = pygame.Surface((W, H), pygame.SRCALPHA)
            ov.fill((0, 0, 0, 120))
            screen.blit(ov, (0, 0))
            gt = font.render("GAME OVER", True, OBSTACLE)
            screen.blit(gt, (W // 2 - gt.get_width() // 2, H // 2 - 40))
            msg = "spike to restart" if serial else "SPACE to restart"
            rt = small_font.render(msg, True, DIM)
            screen.blit(rt, (W // 2 - rt.get_width() // 2, H // 2 + 10))

        elif not started:
            msg = "spike to start" if serial else "SPACE to start"
            st = small_font.render(msg, True, ACCENT)
            screen.blit(st, (W // 2 - st.get_width() // 2, GROUND_Y - 80))

        pygame.display.flip()

    return "quit"

def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Serial Jump")
    clock = pygame.time.Clock()

    try:
        font       = pygame.font.SysFont("couriernew", 28, bold=True)
        small_font = pygame.font.SysFont("couriernew", 15)
    except Exception:
        font       = pygame.font.SysFont(None, 32, bold=True)
        small_font = pygame.font.SysFont(None, 18)

    while True:
        port, baud = port_select_screen(screen, clock, font, small_font)

        serial = None
        if port:
            serial = SerialReader(port, baud)
            serial.start()

        result = game(screen, clock, font, small_font, serial)

        if serial:
            serial.stop()

        if result == "quit":
            break

    pygame.quit()

if __name__ == "__main__":
    main()