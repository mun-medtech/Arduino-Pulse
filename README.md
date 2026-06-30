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

---

## Part 2: Installing Python and Setup `pip`

### Step 2.1: Download Python

1. Go to the official [Python Downloads for Windows](https://www.python.org/downloads/windows/) page.
2. Click the yellow button that says **"Download Python 3.x.x"** (the latest stable version). This downloads an installer package like `python-3.x.x-amd64.exe`.

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

### Note: The EKG sensor should be wire to pins 3.3v, GND, and A0 on an Arduino UNO!

### Troubleshooting Environment Variables

If you receive an error stating *'python' is not recognized as an internal or external command*, the PATH checkbox was likely missed during installation.

* **Fix:** Re-run the downloaded Python installer file, choose **Modify**, and ensure the **"Add Python to environment variables"** or **"PATH"** option is checked on the advanced options page.
