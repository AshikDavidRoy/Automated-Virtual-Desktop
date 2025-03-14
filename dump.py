import pyautogui
import subprocess
import time
import sys
import os

# Configuration
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
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
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'win', 'f4')
        time.sleep(1)
    for _ in range(5):  # Adjust based on your system
        pyautogui.hotkey('ctrl', 'win', 'left')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'win', 'f4')
        time.sleep(1)

# Function to create a new virtual desktop
def create_virtual_desktop():
    pyautogui.hotkey('ctrl', 'win', 'd')
    time.sleep(1)

# Main setup function
def setup_virtual_desktops():
    remove_all_virtual_desktops()
    
    # Create desktops and open websites
    create_virtual_desktop()
    open_website(WEBSITES["Spotify"])
    time.sleep(2)

    create_virtual_desktop()
    open_website(WEBSITES["ChatGPT"])
    time.sleep(2)
    open_website(WEBSITES["Gemini"], new_window=False)
    time.sleep(2)
    open_website(WEBSITES["DeepSeek"])
    time.sleep(2)

    create_virtual_desktop()
    open_website(WEBSITES["CodeChef"])
    time.sleep(1.5)
    open_website(WEBSITES["LeetCode"], new_window=False)
    time.sleep(1.5)

    create_virtual_desktop()
    open_website(WEBSITES["GitHub"])
    time.sleep(1.5)

    # Switch back to the first desktop
    for _ in range(7):
        pyautogui.hotkey('ctrl', 'win', 'left')
        time.sleep(0.5)

# Run the setup
if __name__ == "__main__":
    setup_virtual_desktops()











import pyautogui
import subprocess
import time
# Function to open an application
def open_app(app_path):
    subprocess.Popen(app_path)

# Function to open a website in a new Brave browser window
def open_website(url, new_window=True):
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" # Any other Browser path you prefer
    if new_window:
        # Open the URL in a new browser window
        subprocess.Popen([brave_path, '--new-window', url])
    else:
        # Open the URL in the same browser window
        subprocess.Popen([brave_path, '--', url])
# Function to remove all virtual desktops except one
def remove_all_virtual_desktops():
    # Move to the right and close each desktop up to 15 times
    for _ in range(7):
        pyautogui.hotkey('ctrl', 'win', 'right')
        # time.sleep(0.5)  # Small delay to ensure desktop switch
        pyautogui.hotkey('ctrl', 'win', 'f4')
        # time.sleep(0.5)  # Small delay to ensure desktop close

    # Move to the left and close each desktop up to 5 times
    for _ in range(5):
        pyautogui.hotkey('ctrl', 'win', 'left')
        # time.sleep(0.5)  # Small delay to ensure desktop switch
        pyautogui.hotkey('ctrl', 'win', 'f4')
        # time.sleep(0.5)  # Small delay to ensure desktop close

# Function to create a new virtual desktop
def create_virtual_desktop():
    pyautogui.hotkey('ctrl', 'win', 'd')
    # time.sleep(1)  # Give some time for the desktop to be created

# Function to handle the virtual desktops and application setup
def setup_virtual_desktops():
    # Remove all but one virtual desktop
    remove_all_virtual_desktops()
    
    # Create and set up virtual desktops
    # create_virtual_desktop()  # Create the first additional desktop
    pyautogui.hotkey('ctrl', 'shift','alt', 'm')
    time.sleep(2)
    open_website("https://open.spotify.com/")
    time.sleep(2)
    # pyautogui.hotkey('shift','win', 'left')
    time.sleep(3)

    create_virtual_desktop()  # Create the second additional desktop
    # open_app(r'code_editors_path.exe')  # Replace with your code editor's path
    pyautogui.hotkey('ctrl','shift','alt', 'v')
    time.sleep(3)
    create_virtual_desktop()  # Create the additional desktop
    open_website("https://chatgpt.com/")  # Replace with your chat app's URL
    time.sleep(2)
    open_website("https://gemini.google.com/app?hl=en-IN", new_window=False)  # Replace with your chat app's URL
    time.sleep(2)
    open_website("https://chat.deepseek.com/")
    time.sleep(2)
    # pyautogui.hotkey('shift','win', 'left')

    create_virtual_desktop()  # Create the third additional desktop
    open_website("https://www.codechef.com/")
    time.sleep(1.5)
    open_website("https://leetcode.com/", new_window=False)
    time.sleep(1.5)

    create_virtual_desktop()  # Create the fourth additional desktop
    open_website("https://github.com/<username>")  # Replace with your GitHub profile URL
    time.sleep(1.5)
    # pyautogui.hotkey('shift','win', 'left')

    for _ in range(5):
        pyautogui.hotkey('ctrl', 'win', 'left')

# Directly set up the virtual desktops and applications
setup_virtual_desktops()




















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
