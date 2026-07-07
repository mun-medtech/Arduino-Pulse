# 🦖 EKG Dino Game — Setup Guide
### Windows Computers | Elementary–High School

Welcome! You're about to set up your own heartbeat-powered Dino Game. Follow these steps **in order**, and don't skip any — each one builds on the last. If something doesn't look right, check the "Uh oh, help!" boxes along the way.

---

## ✅ What You'll Need Before Starting
- A Windows computer
- Your Arduino UNO board
- A USB cable to connect it
- Your EKG sensor
- The project folder (with `read.ino`, `requirements.txt`, and the `gui` folder inside it)

---

## Part 1: Install the Arduino IDE

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

> 🔌 **Wiring reminder:** Your EKG sensor connects to the Arduino UNO like this:
> | EKG Sensor Pin | Arduino UNO Pin |
> |---|---|
> | + / VCC | 3.3V |
> | – / GND | GND |
> | Signal | A0 |

### 🆘 Uh oh, help!
- **Nothing happens when I double-click the installer:** Right-click it and choose "Run as administrator."
- **I don't see a driver prompt:** That's okay — some versions install drivers automatically.

---

## Part 2: Open and Upload `read.ino`

Now let's load the code that reads your heartbeat sensor onto the board.

1. Open the **Arduino IDE** (if it's not already open).
2. Click **File → Open...**
3. Navigate to your project folder and select **`read.ino`**. Click **Open**.
4. Plug your **Arduino UNO** into the computer with the USB cable.
5. At the top of the Arduino IDE, click the **board/port dropdown** and select:
   - Board: **Arduino UNO**
   - Port: the one that says something like **COM3 (Arduino UNO)** — the exact number may differ.
6. Click the **Upload** button (the right-facing arrow icon, top-left).
7. Watch the bottom of the window. Wait for the message **"Done uploading."**

### 🆘 Uh oh, help!
- **I don't see any COM port:** Unplug and replug the USB cable. Try a different USB port.
- **"Upload error" or "Failed to open port":** Close any other program that might be using the Arduino (like a Serial Monitor), then try again.
- **Nothing in the port dropdown looks right:** Ask a teacher or adult to check Device Manager for a "USB Serial Device."

---

## Part 3: Install Python and `pip`

Python is the language that runs the Dino Game itself.

1. Go to **https://www.python.org/downloads/windows/**
2. Click the yellow **"Download Python 3.x.x"** button.
3. Open the downloaded file.
4. ⚠️ **Very important:** At the bottom of the first screen, **check the box that says "Add python.exe to PATH."** If you miss this, nothing else will work!
5. Click **Install Now**.
6. If you see an option to **"Disable path length limit"** at the end, click it, then click **Close**.

### Check that it worked
1. Press the **Windows key**, type `cmd`, and press **Enter**.
2. Type this and press Enter:
   ```
   python --version
   ```
   You should see something like `Python 3.x.x`.
3. Type this and press Enter:
   ```
   pip --version
   ```
   You should see a version number too.

### 🆘 Uh oh, help!
- **It says "'python' is not recognized":** You probably missed the PATH checkbox. Re-run the Python installer, choose **Modify**, and make sure **"Add Python to environment variables"** is checked.

---

## Part 4: Install the Game's Dependencies

"Dependencies" are extra tools the game needs to run (for talking to the Arduino and drawing graphics).

1. In the Command Prompt, navigate to your project folder. For example:
   ```
   cd path\to\your\project_folder
   ```
   (Replace this with wherever your project is saved — for example `cd Desktop\dino_game_project`.)
2. Type this and press Enter:
   ```
   pip install -r requirements.txt
   ```
3. Wait for it to finish. You'll see a list of packages being installed.

### 🆘 Uh oh, help!
- **"No such file or directory":** Make sure you're in the right folder. Type `dir` to see the files there — you should see `requirements.txt` listed.

---

## Part 5: Run the Dino Game!

1. Make sure your Arduino is still plugged in.
2. In the same Command Prompt window, type:
   ```
   python gui/dino_game.py
   ```
3. The Dino Game window should pop up! 🎉

> ⚠️ **Before you play:** Make sure the game connects at a **baud rate of 9600** (same as the sensor). If it asks you to pick a COM port, choose the same one you used in Part 2.

### 🆘 Uh oh, help!
- **The game says it can't find the serial port:** Double check the Arduino is plugged in and that `read.ino` was successfully uploaded (Part 2).
- **The game opens but nothing happens when I move:** Make sure the EKG sensor is wired correctly and touching skin properly.

---

## 🎮 You're Ready!
Once the window pops up and your heartbeat sensor is connected, jump the dino by triggering your heartbeat signal. Have fun!