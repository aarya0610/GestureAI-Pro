import os
import time
import webbrowser
import pyautogui

from assistant import run_assistant

last_action = ""
last_action_time = 0

COOLDOWN = 2


def perform_action(gesture):

    global last_action
    global last_action_time

    current_time = time.time()

    # Prevent repeated actions
    if current_time - last_action_time < COOLDOWN:
        return

    if gesture == last_action:
        return

    if gesture == "One Finger":
        webbrowser.open("https://www.google.com")
        print("✅ Opening Google")

    elif gesture == "Two Fingers":
        webbrowser.open("https://www.youtube.com")
        print("✅ Opening YouTube")

    elif gesture == "Three Fingers":
        os.system("calc")
        print("✅ Opening Calculator")

    elif gesture == "Four Fingers":
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("✅ Screenshot Saved")

    elif gesture == "Open Palm":
        print("🎤 AI Assistant")
        run_assistant()

    last_action = gesture
    last_action_time = current_time