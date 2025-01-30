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
    open_website("https://github.com/AshikDavidRoy")  # Replace with your GitHub profile URL
    time.sleep(1.5)
    # pyautogui.hotkey('shift','win', 'left')

    for _ in range(5):
        pyautogui.hotkey('ctrl', 'win', 'left')

# Directly set up the virtual desktops and applications
setup_virtual_desktops()
