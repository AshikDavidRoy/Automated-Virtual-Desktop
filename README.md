<!-- **README.md** -->

# Project: Automated Virtual Desktop & Application Setup

This Python script automates a streamlined workflow by setting up multiple virtual desktops and opening specific applications on each one.

**Installation**

1. **Prerequisites:** Ensure you have [Python 3](https://www.python.org/downloads/)
2. **Install `pyautogui`:** Open a command prompt or terminal and run the following command:

   ```bash
   pip install pyautogui
   ```

3. **Clone or Download:** Clone this repository using Git or download the files manually.

**Usage (Windows)**

1. **Modify Paths:**
   - Update application paths in `setup_virtual_desktops()` if necessary (e.g., `open_app(r'C:\path\to\your\app.exe')`).
   - Replace chat app URL with the one you prefer.
2. **Run the Script:**
   - Open a command prompt or terminal and navigate to the directory containing `desktop_setup.py`.
   - Execute the script using `python desktop_setup.py` to test the code.

**Code Explanation**

**Libraries:**

- `pyautogui`: Simulates keyboard and mouse actions for automation.
- `subprocess`: Executes external commands from Python (for opening applications).
- `time`: Adds delays between actions for proper execution (optional).

**Functions:**

- `open_app(app_path)`: Launches a specified application using its path.
- `open_website(url, new_window=True)`: Opens a website in a new Brave browser window by default, or in the same window if `new_window=False`.
- `remove_all_virtual_desktops()`: Closes all virtual desktops except for the current one, handling potential variations in closing direction (`ctrl+win+right` vs. `ctrl+win+left`).
- `create_virtual_desktop()`: Creates a new virtual desktop.
- `setup_virtual_desktops()`:
   - Removes all but one virtual desktop (commented out for optional usage).
   - Creates four additional virtual desktops and opens predefined websites/applications:
     - Desktop 1: Spotify and Music Player
     - Desktop 2: ChatGPT and Gemini (user-specified URL)
     - Desktop 3: CodeChef, LeetCode (new window)
     - Desktop 4: GitHub profile
   - Adjust these URLs and paths based on your preferences.

**Batch Script (Optional)**

If you prefer a one-click setup on Windows:

1. **Create a Batch File (cmd_code.bat):**
   - Copy and paste the provided batch script content into a new text file, save it as `cmd_code.bat` in the same directory as your Python script.
2. **Run the Batch File:**
   - Double-click `cmd_code.bat` to automatically navigate to the Python script's directory and execute it.

**Customization**

- Modify the script to tailor it to your specific needs, including application paths, websites, and number of virtual desktops.
- Consider using environment variables or configuration files to manage variable data more effectively.

**Notes**

- The `time.sleep()` delays might require adjustments depending on your system setup.
- Be cautious when using `pyautogui`, as aggressive automation could interfere with other applications.

**Additional Considerations**

- Explore alternative virtual desktop management libraries or operating system-specific tools for more advanced control.
- Consider security implications when automating actions on your system.

**Setting Up a Shortcut Key**

1. **Create a Batch File:**
   - Copy and paste the following code into a new text file and save it as `cmd_code.cmd` in the same directory as your Python script:

   ```batch
   @echo off
   REM Navigate to the directory where your Python script is located
   cd "C:\path\to\your\python\script\directory"

   REM Run the Python script
   python desktop_setup.py

   exit
   ```

2. **Assign a Shortcut Key:**
   - Right-click on the `cmd_code.cmd` file and select "Properties."
   - Go to the "Shortcut" tab.
   - In the "Shortcut key" field, enter "Ctrl+Shift+Alt+S" (without quotes).
   - Click "Apply" and then "OK."

Now, whenever you press "Ctrl+Shift+Alt+S," the batch file will execute, launching your Python script and setting up your virtual desktops and applications.


By following these guidelines, you can effectively use this script to create a customized multi-desktop environment that boosts your productivity.
