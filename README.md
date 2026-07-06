## Part 1: Installing the Arduino IDE

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

---

## Part 3: Verifying the Installations

To make sure both environments are configured properly, use the Windows Command Prompt.

1. Press the **Windows Key**, type `cmd`, and press **Enter** to open the Command Prompt.
2. To verify Python, type the following command and press **Enter**:
```cmd
python --version

```


*Expected Output:* `Python 3.x.x`
3. To verify `pip` (Python's package manager), type the following command and press **Enter**:
```cmd
pip --version

```


*Expected Output:* `pip xx.x from ... (python 3.x)`

### Troubleshooting Environment Variables

If you receive an error stating *'python' is not recognized as an internal or external command*, the PATH checkbox was likely missed during installation.

* **Fix:** Re-run the downloaded Python installer file, choose **Modify**, and ensure the **"Add Python to environment variables"** or **"PATH"** option is checked on the advanced options page.

---

## Part 4: Installing Dependencies via `requirements.txt`

Before running the game, you need to install the project's external Python libraries (such as those needed for serial communication and graphics).

1. Open the Command Prompt (`cmd`).
2. Navigate to your project's root directory (where the `requirements.txt` file is located) using the `cd` command:
```cmd
cd path\to\your\project_folder

```


3. Run the following command to install all necessary dependencies at once:
```cmd
pip install -r requirements.txt

```


4. Wait for the installation to finish. You should see a message indicating successful installation of the packages.

---

## Part 5: Running the Dino Game GUI

Once the Arduino is plugged in and your Python dependencies are installed, you can launch the game.

1. Ensure you are still in your project's root directory in the Command Prompt.
2. Execute the Python script located in the `gui` folder by running:
```cmd
python gui/dino_game.py

```


3. The Dino Game interface should now pop up on your screen.

> ⚠️ **Serial Connection Warning:** Make sure your Arduino is plugged in, and that the game is set to use a baud rate of **9600** (this matches the EKG sensor output rate). If the game asks for a COM port, select the one corresponding to your Arduino UNO.
