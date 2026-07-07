# 🦖 EKG Dino Game — Setup Guide
### Windows Computers | Elementary–High School

### Step 1.1: Download the Installer

1. Open your web browser and navigate to the official [Arduino Software Page](https://www.arduino.cc/en/software).
2. Locate the **Arduino IDE 2.x.x** section (or the latest stable version).
3. Click on the link labeled **"Windows Win 10 and newer, 64 bits"**.
4. On the next page, you can choose to make a donation or click **"JUST DOWNLOAD"** to begin downloading the executable file (e.g., `arduino-ide_2.x.x_Windows_64bit.exe`).

### Step 1.2: Run the Installation Wizard

1. Navigate to your **Downloads** folder and double-click the downloaded `.exe` file.
2. If a *User Account Control (UAC)* prompt appears asking for permission, click **Yes**.
3. **License Agreement:** Read the terms and click **I Agree**.
4. **Installation Options:** Choose whether you want to install the software for *Anyone using this computer* (requires admin privileges) or *Just for me*. Click **Next**.
5. **Choose Install Location:** Leave the default destination folder as is (`C:\Program Files\Arduino IDE`) and click **Install**.

### Step 1.3: Allow Driver Installation & Verify

1. During installation, Windows may prompt you to install device drivers from "Arduino srl" or "Adafruit Industries". **Crucially click "Install"** on these prompts; these drivers allow your computer to communicate with Arduino hardware over USB.
2. Once complete, leave the "Run Arduino IDE" box checked and click **Finish**.
3. Ensure the program opens successfully. If Windows Defender Firewall blocks some features, click **Allow access** for private networks.

> **Hardware & Code Setup:**
> * The EKG sensor should be wired to pins **3.3V**, **GND**, and **A0** on your Arduino UNO.
> * Ensure your Arduino sketch initializes serial communication with **`Serial.begin(9600);`** inside the `setup()` function.

### Step 1.4: Connect the Arduino Uno
 
1. Plug the Arduino Uno into your computer using a USB cable.
2. Windows should automatically detect the board and finish installing drivers in the background (usually indicated by a notification in the bottom-right corner).
### Step 1.5: Select Your Board and Port
 
1. Open the Arduino IDE.
2. Go to **Tools → Board → Arduino AVR Boards → Arduino Uno**.
3. Go to **Tools → Port** and select the COM port your Arduino appears on (e.g., `COM3 (Arduino Uno)` or `COM4 (Arduino Uno)`). This number varies by computer and USB port used.
   - If no port appears under this menu, try a different USB cable or port, and confirm the drivers installed correctly in Step 1.3.
### Step 1.6: Write or Open Your Sketch
 
If your project doesn't already include an `.ino` file, paste the following basic EMG-reading sketch into a new sketch window:
 
```cpp
void setup() {
  Serial.begin(9600);
}
 
void loop() {
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  delay(10);
}
```
 
Save the sketch (**File → Save**) before uploading.
 
### Step 1.7: Flash (Upload) the Sketch
 
1. Click the **right-arrow "Upload" icon** in the top-left toolbar.
3. It will then upload to the board. Watch for the small **TX/RX LEDs** on the Arduino to blink rapidly, this confirms data is transferring.
4. When finished, the IDE displays **"Done uploading."** in the status bar.
**Troubleshooting: "Access is denied" / "unable to open port" errors during upload**
 
This means another program is already holding the COM port open, blocking the IDE from using it. Before retrying:
- Close any open **Serial Monitor** or **Serial Plotter** window.
- Stop any running Python script that might be reading the serial port (`Ctrl+C` in its terminal).
- Close other programs that might use serial ports (PuTTY, VS Code serial extensions, a second Arduino IDE window).
- If it still fails, unplug and replug the Arduino's USB cable, then try uploading again.

---

## Part 2: Installing Python and Setting Up `pip`

### Step 2.1: Download Python

1. Go to the official [Python 3.12 downloads page](https://www.python.org/downloads/release/python-3120/) (or the latest 3.12.x patch release).
2. Scroll to the **Files** section and click **Windows installer (64-bit)**.

### Step 2.2: Execute the Installer (Critical Step)

1. Double-click the downloaded Python installer file.
2. **CRITICAL STEP:** At the bottom of the installation window, check the box that says **"Add python.exe to PATH"**. If you skip this, your command prompt will not recognize Python or `pip` commands.
3. Check the box for **"Use admin privileges when installing py.exe"** (if available).
4. Click **Install Now** at the top of the window.

### Step 2.3: Disable Path Length Limit (Optional but Recommended)

1. At the very end of the installation process, the wizard may show an option that says **"Disable path length limit"**.
2. Click this option. It prevents Windows from running into errors later on if Python packages are buried deep within nested folders.
3. Click **Close**.
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

> ⚠️ **Serial Connection Warning:** Make sure your Arduino is plugged in, and that the game is set to use a baud rate of **9600** (this matches the EKG sensor output rate). If the game asks for a COM port, select the one corresponding to your Arduino UNO.
## Part 4: Install the Game's Dependencies

"Dependencies" are extra tools the game needs to run (for talking to the Arduino and drawing graphics).

1. In the Command Prompt, navigate to your project folder. For example:
   ```
   cd path\to\your\project\Arduino-Pulse
   ```
   (Replace this with wherever your project is saved — for example `cd Desktop\Arduino-Pulse`.)
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
   python dino_game.py
   ```
3. The Dino Game window should pop up! 🎉

> ⚠️ **Before you play:** Make sure the game connects at a **baud rate of 9600** (same as the sensor). If it asks you to pick a COM port, choose the same one you used in Part 2.

### 🆘 Uh oh, help!
- **The game says it can't find the serial port:** Double check the Arduino is plugged in and that `read.ino` was successfully uploaded (Part 2).
- **The game opens but nothing happens when I move:** Make sure the EKG sensor is wired correctly and touching skin properly.

---

## 🎮 You're Ready!
Once the window pops up and your heartbeat sensor is connected, jump the dino by triggering your heartbeat signal. Have fun!
