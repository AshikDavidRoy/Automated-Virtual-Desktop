import pyautogui
import subprocess
import time

# Configuration
BRAVE_PATH = r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
VS_CODE_PATH = r"C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Update path if needed

WEBSITES = {
    "Spotify": "https://open.spotify.com/",
    "ChatGPT": "https://chatgpt.com/",
    "Gemini": "https://gemini.google.com/app?hl=en-IN",
    "DeepSeek": "https://chat.deepseek.com/",
    "CodeChef": "https://www.codechef.com/",
    "LeetCode": "https://leetcode.com/",
    "GitHub": "https://github.com/<username>",  # Replace with your GitHub username
    "Video": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/"
        # Add more video URLs here
    ]
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

# Function to open multiple video links
def open_video_links(video_links):
    for link in video_links:
        open_website(link, new_window=False)  # Opens in same Brave window as new tabs
        time.sleep(1)

# Function to remove all virtual desktops
def remove_all_virtual_desktops():
    for _ in range(7):  # Move right and close desktops
        pyautogui.hotkey('ctrl', 'win', 'right')
        pyautogui.hotkey('ctrl', 'win', 'f4')
    for _ in range(5):  # Move left and close remaining
        pyautogui.hotkey('ctrl', 'win', 'left')
        pyautogui.hotkey('ctrl', 'win', 'f4')

# Function to create a new virtual desktop
def create_virtual_desktop():
    pyautogui.hotkey('ctrl', 'win', 'd')
    time.sleep(1)

# Main setup function
def setup_virtual_desktops():
    remove_all_virtual_desktops()

    # Desktop 1: Music and Videos
    pyautogui.hotkey('ctrl', 'shift', 'alt', 'm')
    time.sleep(3)
    open_website(WEBSITES["Spotify"])
    time.sleep(2)
    open_video_links(WEBSITES["Video"])  # Open videos in new tabs
    time.sleep(2)

    # Desktop 2: VS Code
    create_virtual_desktop()
    open_app(VS_CODE_PATH)
    pyautogui.hotkey('ctrl', 'shift', 'alt', 'v')
    time.sleep(5)

    # Desktop 3: AI Chat tools
    create_virtual_desktop()
    open_website(WEBSITES["ChatGPT"])
    time.sleep(2)
    open_website(WEBSITES["DeepSeek"])
    time.sleep(2)

    # Desktop 4: GitHub
    create_virtual_desktop()
    open_website(WEBSITES["GitHub"])
    time.sleep(1)

    # Return to first desktop
    for _ in range(8):
        pyautogui.hotkey('ctrl', 'win', 'left')

# Run the setup
if __name__ == "__main__":
    setup_virtual_desktops()
