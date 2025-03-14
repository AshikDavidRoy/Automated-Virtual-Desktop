import pyautogui
import subprocess
import time

# Configuration
BRAVE_PATH = r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
VS_CODE_PATH = r"C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # VS Code path
WEBSITES = {
    "Spotify": "https://open.spotify.com/",
    "ChatGPT": "https://chatgpt.com/",
    "Gemini": "https://gemini.google.com/app?hl=en-IN",
    "DeepSeek": "https://chat.deepseek.com/",
    "CodeChef": "https://www.codechef.com/",
    "LeetCode": "https://leetcode.com/",
    "GitHub": "https://github.com/<username>",  # Replace with your username
}

# Function to open an application
def open_app(app_path):
    try:
        subprocess.Popen(app_path)
    except Exception as e:
        print(f"Error opening application: {e}")

# Function to open a website
def open_website(url, new_window=True):
    try:
        if new_window:
            subprocess.Popen([BRAVE_PATH, '--new-window', url])
        else:
            subprocess.Popen([BRAVE_PATH, '--', url])
    except Exception as e:
        print(f"Error opening website: {e}")

# Function to remove all virtual desktops
def remove_all_virtual_desktops():
    for _ in range(7):  # Adjust based on your system
        pyautogui.hotkey('ctrl', 'win', 'right')
        # time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'win', 'f4')
        # time.sleep(1)
    for _ in range(5):  # Adjust based on your system
        pyautogui.hotkey('ctrl', 'win', 'left')
        # time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'win', 'f4')
        # time.sleep(1)

# Function to create a new virtual desktop
def create_virtual_desktop():
    pyautogui.hotkey('ctrl', 'win', 'd')
    time.sleep(1)

# Main setup function
def setup_virtual_desktops():
    remove_all_virtual_desktops()
    
    # Create desktops and open websites
    pyautogui.hotkey('ctrl', 'shift', 'alt', 'm')
    time.sleep(3)
    open_website(WEBSITES["Spotify"])
    time.sleep(2)

    create_virtual_desktop()
    open_app(VS_CODE_PATH)  # Open VS Code
    time.sleep(5)  # Give VS Code time to launch

    create_virtual_desktop()
    open_website(WEBSITES["ChatGPT"])
    time.sleep(2)
    open_website(WEBSITES["DeepSeek"])
    time.sleep(2)

    create_virtual_desktop()
    open_website(WEBSITES["GitHub"])
    time.sleep(1)

    # Switch back to the first desktop
    for _ in range(8):
        pyautogui.hotkey('ctrl', 'win', 'left')
        # time.sleep(0.5)

# Run the setup
if __name__ == "__main__":
    setup_virtual_desktops()
