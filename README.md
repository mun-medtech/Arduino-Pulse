# 🦖 EMG Dino Game — Setup Guide
### Windows Computers | Elementary–High School

Welcome! You're about to set up your own muscle-powered Dino Game. Follow these steps **in order**, and don't skip any — each one builds on the last. If something doesn't look right, check the "Uh oh, help!" boxes along the way.

---

## ✅ What You'll Need Before Starting
- A Windows computer
- Your Arduino UNO board
- A USB cable to connect it
- Your MyoWare EMG sensor

---

## Part 1: Install Git and Get the Project Files

Git is a tool that lets you download ("clone") a copy of the project's code onto your computer.

### Step 1.1: Install Git

1. Go to **https://git-scm.com/downloads/win**
2. Click **"Click here to download"** to get the 64-bit Windows installer.
3. Double-click the downloaded file to run it.
4. Click **Next** through the setup screens — the default options are fine for this project. Click **Install** when you reach that screen.
5. Click **Finish** when it's done.

### Step 1.2: Clone the Repo

1. Press the **Windows key**, type `cmd`, and press **Enter** to open the Command Prompt.
2. Navigate to where you want the project saved, for example your Desktop:
   ```cmd
   cd Desktop
   ```
3. Type the following, replacing the URL with your project's actual repo link, and press Enter:
   ```cmd
   git clone https://github.com/mun-medtech/Arduino-Pulse.git
   ```
4. This creates a new folder containing all the project files, including `read.ino`, `requirements.txt`, and the `gui` folder.
5. Move into the new folder:
   ```cmd
   cd Arduino-Pulse
   ```

### 🆘 Uh oh, help!
- **"'git' is not recognized":** Close and reopen the Command Prompt (Git needs a fresh window after installing to update PATH). If it still doesn't work, re-run the Git installer.
- **I don't have a repo link:** Ask your teacher or whoever shared this project with you for the GitHub link.

---

## Part 2: Install the Arduino IDE

The Arduino IDE is the program that lets your computer "talk" to your Arduino board.

1. Open a web browser and go to **https://www.arduino.cc/en/software**
2. Find the **Arduino IDE 2.x** section.
3. Click **"Windows Win 10 and newer, 64 bits"**.
4. On the next page, click **"JUST DOWNLOAD"** (no need to donate).
5. Go to your **Downloads** folder and double-click the file you just downloaded (it ends in `.exe`).
6. If a window pops up asking for permission, click **Yes**.
7. Click **I Agree** on the license page.
8. Choose **"Just for me"** (unless a teacher tells you otherwise), then click **Next**.
9. Leave the install location as-is, and click **Install**.
10. Windows may ask if it's okay to install a "driver" from Arduino — **always click Install** on these. This is what lets your computer recognize the board.
11. When it's done, leave **"Run Arduino IDE"** checked and click **Finish**.
12. If a firewall message pops up, click **Allow access**.

> 🔌 **Wiring reminder:** Your MyoWare EMG sensor connects to the Arduino UNO like this:
> | MyoWare Sensor Pin | Arduino UNO Pin |
> |---|---|
> | + / VCC | 3.3V |
> | – / GND | GND |
> | Signal (SIG) | A0 |

### 🆘 Uh oh, help!
- **Nothing happens when I double-click the installer:** Right-click it and choose "Run as administrator."
- **I don't see a driver prompt:** That's okay — some versions install drivers automatically.

---

## Part 3: Open and Upload `read.ino`

Now let's load the code that reads your muscle sensor onto the board.

1. Open the **Arduino IDE** (if it's not already open).
2. Click **File → Open...**
3. Navigate to your project folder (the one you cloned in Part 1) and select **`read.ino`**. Click **Open**.
4. Plug your **Arduino UNO** into the computer with the USB cable. (Make sure it's a real data cable — some USB cables only charge and can't send data!)
5. At the top of the Arduino IDE, click the **board/port dropdown** and select:
   - Board: **Arduino UNO**
   - Port: the one that says something like **COM3 (Arduino UNO)** — the exact number may differ.
6. Click the **Upload** button (the right-facing arrow icon, top-left).
7. Watch the bottom of the window. You'll see a compiling message first, then wait for **"Done uploading."**
8. To double-check it worked, open **Tools → Serial Monitor** (set the dropdown in the bottom-right to **9600 baud**). You should see a stream of numbers. Try flexing the muscle the sensor is attached to — the numbers should jump up when you flex and settle back down when you relax.

### Checking the Arduino's Port from the Command Prompt

If you're not sure which COM port your Arduino is using — or want to double check it matches what you selected in the Arduino IDE — you can find it from the Command Prompt (this only works once Python is installed; see Part 4 below):

```cmd
python -c "import serial.tools.list_ports; [print(p) for p in serial.tools.list_ports.comports()]"
```

This prints every serial device your computer can see, something like:
```
COM3 - USB-SERIAL CH340 (COM3)
```
The `COM3` part is the port number you'll need — it should match the port you selected in the Arduino IDE, and it's what the game will connect to when you run it later.

### 🆘 Uh oh, help!
- **I don't see any COM port:** Unplug and replug the USB cable. Try a different USB port.
- **"Upload error," "Failed to open port," or "Access is denied":** This means something else is already using that port. Close any open Serial Monitor windows and stop any Python scripts that might be running, then try uploading again. If it still won't work, unplug and replug the Arduino and try once more.
- **Nothing in the port dropdown looks right:** Ask a teacher or adult to check Device Manager for a "USB Serial Device."
- **The numbers in Serial Monitor don't change when I flex:** Check that all three wires (VCC, GND, Signal) are firmly connected, and that the sensor's electrode pads are pressed against skin, not clothing.

---

## Part 4: Install Python and `pip`

Python is the language that runs the Dino Game itself.

> ⚠️ **Important:** Install **Python 3.12** specifically, not the newest version. Some of the game's tools don't have ready-to-go installers for the very latest Python yet, which can cause confusing errors. Python 3.12 is fully supported and works great.

1. Go to **https://www.python.org/downloads/release/python-3120/** (or the newest 3.12.x version listed there).
2. Scroll down to **Files** and click **Windows installer (64-bit)**.
3. Open the downloaded file.
4. ⚠️ **Very important:** At the bottom of the first screen, **check the box that says "Add python.exe to PATH."** If you miss this, nothing else will work!
5. Click **Install Now**.
6. If you see an option to **"Disable path length limit"** at the end, click it, then click **Close**.

### Check that it worked

1. Press the **Windows key**, type `cmd`, and press **Enter**.
2. Type this and press Enter:
   ```cmd
   python --version
   ```
   You should see something like `Python 3.12.x`.
3. Type this and press Enter:
   ```cmd
   pip --version
   ```
   You should see a version number too.

### 🆘 Uh oh, help!
- **It says "'python' is not recognized":** You probably missed the PATH checkbox during install. Re-run the Python installer, choose **Modify**, and make sure **"Add Python to environment variables"** is checked.
- **It shows a much newer version, like 3.13 or 3.14:** You may have an older Python already installed. That's usually fine to leave alone — just make sure you use `py -3.12` instead of `python` in the next steps if `python --version` doesn't show 3.12.

---

## Part 5: Install the Game's Dependencies

"Dependencies" are extra tools the game needs to run (for talking to the Arduino and drawing graphics).

1. In the Command Prompt, navigate to your project folder (the one you cloned in Part 1):
   ```cmd
   cd Desktop\Arduino-Pulse
   ```
2. Type this and press Enter:
   ```cmd
   pip install -r requirements.txt
   ```
3. Wait for it to finish. You'll see a list of packages being installed.

### 🆘 Uh oh, help!
- **"No such file or directory":** Make sure you're in the right folder. Type `dir` to see the files there — you should see `requirements.txt` listed.
- **Errors mentioning "building a wheel" or a missing compiler:** This usually means Python installed isn't 3.12. Double check with `python --version` and revisit Part 4 if needed.

---

## Part 6: Run the Dino Game!

1. Make sure your Arduino is still plugged in and `read.ino` has already been uploaded (Part 3).
2. **Close the Arduino IDE's Serial Monitor** if you left it open — the game needs the port to itself.
3. In the same Command Prompt window, type:
   ```cmd
   python gui/dino_game.py
   ```
4. The Dino Game window should pop up! 🎉

> ⚠️ **Before you play:** Make sure the game connects at a **baud rate of 9600** (same as the sensor). If it asks you to pick a COM port, choose the same one you found using the command in Part 3 (or the one you selected in the Arduino IDE).

### 🆘 Uh oh, help!
- **The game says it can't find the serial port:** Double check the Arduino is plugged in and that `read.ino` was successfully uploaded (Part 3), and that no other program (like Serial Monitor) is holding the port open.
- **The game opens but nothing happens when I move:** Make sure the MyoWare sensor is wired correctly and the electrode pads are touching skin properly, not clothing.

---

## 🎮 You're Ready!
Once the window pops up and your muscle sensor is connected, jump the dino by flexing your muscle. Have fun!
