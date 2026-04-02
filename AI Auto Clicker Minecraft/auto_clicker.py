import pyautogui
import keyboard
import time

# first state
is_clicking = False

def toggle_clicker():
    global is_clicking
    is_clicking = not is_clicking
    status = "ON" if is_clicking else "OFF"
    print(f"Auto Clicker is now {status}")

# hotkey keybind
keyboard.add_hotkey('u', toggle_clicker)

print("Press 'u' to toggle the Auto Clicker ON/OFF")
print("Press 'g' to exit the program")

while True:
    if keyboard.is_pressed('g'):
        print("Exiting Auto Clicker...")
        break

    if is_clicking:
        pyautogui.click(button='left')
        time.sleep(0.7)
    else:
        time.sleep(0.1)

        pyautogui.FAILSAFE = True
