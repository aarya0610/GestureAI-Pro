import cv2
import time
import numpy as np
import pyautogui

from hand_tracker import HandTracker
from gesture_controller import GestureController
from mouse_controller import MouseController
from web_launcher import WebLauncher
from app_launcher import AppLauncher
from screenshot_controller import ScreenshotController
from volume_controller import set_volume
from scroll_controller import ScrollController
from brightness_controller import set_brightness
import media_controller
from air_canvas import AirCanvas

# ------------------------------
# Camera Settings
# ------------------------------

WIDTH = 1280
HEIGHT = 720

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

# ------------------------------
# Initialize Modules
# ------------------------------

tracker = HandTracker(
    maxHands=1,
    detectionCon=0.75,
    trackCon=0.75
)

gesture = GestureController()

screen_width, screen_height = pyautogui.size()

mouse = MouseController(screen_width, screen_height)
web = WebLauncher()
apps = AppLauncher()
screenshot = ScreenshotController()
scroll = ScrollController()
canvas = AirCanvas(WIDTH, HEIGHT)

last_action = ""
last_action_time = 0
volume_percent = 0
brightness_percent = 0
ACTION_DELAY = 2  # seconds

# -----------------------------
# Volume Mode
# -----------------------------

frame_reduction = 100
smoothening = 7

previous_x = 0
previous_y = 0

current_x = 0
current_y = 0

previous_time = 0

# ------------------------------
# Main Loop
# ------------------------------

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = tracker.findHands(img)

    lmList = tracker.findPosition(img)

    currentGesture ="NONE"
    if len(lmList) != 0:

        fingers = gesture.fingersUp(lmList)
        currentGesture = gesture.detectGesture(fingers)
        print(currentGesture)
    

        current = time.time()

    # -----------------------------
    # Mouse Move
    # -----------------------------
    if currentGesture == "MOUSE":

        x, y = lmList[8][1], lmList[8][2]
        mouse.move(x, y, WIDTH, HEIGHT)

    # -----------------------------
    # Volume Control
    # -----------------------------
    elif currentGesture == "VOLUME":

        x1, y1 = lmList[4][1], lmList[4][2]   # Thumb
        x2, y2 = lmList[8][1], lmList[8][2]   # Index

        distance = gesture.findDistance((x1, y1), (x2, y2))

        volume_percent = int(np.interp(distance, [30, 220], [0, 100]))

        set_volume(volume_percent)

        cv2.putText(
            img,
            f"Volume : {volume_percent}%",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
       )

        last_action = f"Volume {volume_percent}%"

    # -----------------------------
    # Brightness Control
    # -----------------------------
    elif currentGesture == "BRIGHTNESS":

            x1, y1 = lmList[4][1], lmList[4][2]   # Thumb
            x2, y2 = lmList[12][1], lmList[12][2] # Middle Finger

            distance = gesture.findDistance((x1, y1), (x2, y2))

            brightness_percent = int(np.interp(distance, [30, 220], [0, 100]))
            print(brightness_percent)

            set_brightness(brightness_percent)

            cv2.putText(
                img,
                f"Brightness : {brightness_percent}%",
                (500, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 0, 255),
                3
       )

            last_action = f"Brightness {brightness_percent}%"

    # -----------------------------
    # Play / Pause
    # -----------------------------
    elif currentGesture == "PLAY_PAUSE":

        if current - last_action_time > ACTION_DELAY:
            media_controller.play_pause()
            last_action = "Play / Pause"
            last_action_time = current


    # -----------------------------
    # Next Track
    # -----------------------------
    elif currentGesture == "NEXT_TRACK":

        if current - last_action_time > ACTION_DELAY:
            media_controller.next_track()
            last_action = "Next Track"
            last_action_time = current


    # -----------------------------
    # Previous Track
    # -----------------------------
    elif currentGesture == "PREVIOUS_TRACK":

        if current - last_action_time > ACTION_DELAY:
            media_controller.previous_track()
            last_action = "Previous Track"
            last_action_time = current        

        # -----------------------------
        # Left Click
        # -----------------------------
    elif currentGesture == "LEFT_CLICK":

        if current - last_action_time > ACTION_DELAY:
            mouse.left_click()
            last_action = "Left Click"
            last_action_time = current

        # -----------------------------
        # Right Click
        # -----------------------------
    elif currentGesture == "RIGHT_CLICK":

            if current - last_action_time > ACTION_DELAY:
                mouse.right_click()
                last_action = "Right Click"
                last_action_time = current

        # -----------------------------
        # Double Click
        # -----------------------------
    elif currentGesture == "DOUBLE_CLICK":

            if current - last_action_time > ACTION_DELAY:
                mouse.double_click()
                last_action = "Double Click"
                last_action_time = current

        # -----------------------------
        # Google
        # -----------------------------
    elif currentGesture == "GOOGLE":

     if current - last_action_time > ACTION_DELAY:

          print("Google block reached")

          result = web.open("google")

          print("Result =", result)

          last_action = "Google"

          last_action_time = current
        

        # -----------------------------
        # YouTube
        # -----------------------------
    elif currentGesture == "YOUTUBE":

     if current - last_action_time > ACTION_DELAY:

            print("YOUTUBE BLOCK")

            result = web.open("youtube")

            print("Result =", result)

            last_action = "YouTube"
            last_action_time = current

        # -----------------------------
        # ChatGPT
        # -----------------------------
    elif currentGesture == "CHATGPT":

     if current - last_action_time > ACTION_DELAY:

               print("CHATGPT BLOCK")

               result = web.open("chatgpt")

               print("Result =", result)

               last_action = "ChatGPT"
               last_action_time = current
        # -----------------------------
        # GitHub
        # -----------------------------
    elif currentGesture == "GITHUB":

     if current - last_action_time > ACTION_DELAY:
                web.open("github")
                last_action = "GitHub"
                last_action_time = current

        # -----------------------------
        # LinkedIn
        # -----------------------------
     elif currentGesture == "LINKEDIN":

      if current - last_action_time > ACTION_DELAY:
                web.open("linkedin")
                last_action = "LinkedIn"
                last_action_time = current

     elif currentGesture == "CALCULATOR":

      if current - last_action_time > ACTION_DELAY:
               apps.open_calculator()
               last_action = "Calculator"
               last_action_time = current

     elif currentGesture == "NOTEPAD":

      if current - last_action_time > ACTION_DELAY:
              apps.open_notepad()
              last_action = "Notepad"
              last_action_time = current

    elif currentGesture == "EXPLORER":
           
     if current - last_action_time > ACTION_DELAY:
              apps.open_explorer()
              last_action = "Explorer"
              last_action_time = current

    elif currentGesture == "PAINT":

     if current - last_action_time > ACTION_DELAY:
              apps.open_paint()
              last_action = "Paint"
              last_action_time = current

        # -----------------------------
        # Screenshot
        # -----------------------------
     elif currentGesture == "SCREENSHOT":

      if current - last_action_time > ACTION_DELAY:

             path = screenshot.take_screenshot()

             print(f"Screenshot Saved: {path}")

             last_action = "Screenshot"

             last_action_time = current

        # -----------------------------
        # Scroll
        # -----------------------------
     elif currentGesture == "SCROLL":

            y = lmList[12][2]

            if y < HEIGHT // 2:
                scroll.scroll_up()
                last_action = "Scroll Up"

            else:
                scroll.scroll_down()
                last_action = "Scroll Down"
       
     cv2.putText(
        img,
        f"Last Action : {last_action}",
        (20, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.rectangle(
        img,
        (frame_reduction, frame_reduction),
        (WIDTH - frame_reduction, HEIGHT - frame_reduction),
        (255, 0, 255),
        2
    )

    current_time = time.time()

    fps = 1 / (current_time - previous_time) if previous_time != 0 else 0

    previous_time = current_time

    # -----------------------------
    # Professional HUD
    # -----------------------------
    cv2.rectangle(img, (10, 10), (360, 220), (35, 35, 35), -1)
    cv2.rectangle(img, (10, 10), (360, 220), (0, 255, 255), 2)

    # Title
    cv2.putText(
        img,
        "Gesture AI Pro v2",
        (25, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    # Gesture
    cv2.putText(
        img,
        f"Gesture : {currentGesture}",
        (25,75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    # Last Action
    cv2.putText(
        img,
        f"Last : {last_action}",
        (25,110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
       (255,255,255),
       2
    )

    # Status
    cv2.putText(
        img,
        f"FPS : {int(fps)}",
        (25,145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0,255,0),
        2
   )
    
    # Version
    cv2.putText(
        img,
        "Mode : NORMAL",
        (25,180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,200,0),
        2
   )
    
    # ==========================================
    # Volume Bar
    # ==========================================

    cv2.putText(
        img,
        "Volume",
        (420, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    cv2.rectangle(img, (420,50), (670,75), (70,70,70), -1)

    cv2.rectangle(
        img,
        (420,50),
        (420 + int(volume_percent*2.5),75),
        (0,255,0),
        -1
    )

    cv2.putText(
        img,
        f"{volume_percent}%",
        (680,70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2 
    )

    # ==========================================
    # Brightness Bar
    # ==========================================

    cv2.putText(
        img,
        "Brightness",
        (420,110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    cv2.rectangle(img,(420,125),(670,150),(70,70,70),-1)

    cv2.rectangle(
        img,
        (420,125),
        (420 + int(brightness_percent*2.5),150),
        (0,255,255),
        -1
    )

    cv2.putText(
        img,
        f"{brightness_percent}%",
        (680,145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
   )

    cv2.imshow("Gesture AI Pro v3", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()