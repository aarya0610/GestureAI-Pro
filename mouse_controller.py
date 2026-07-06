import pyautogui
import numpy as np


class MouseController:

    def __init__(self, screen_width, screen_height,
                 frame_reduction=100, smoothening=7):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.frame_reduction = frame_reduction
        self.smoothening = smoothening

        self.prev_x = 0
        self.prev_y = 0

        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0

    def move(self, x, y, cam_width, cam_height):

        x3 = np.interp(
            x,
            (self.frame_reduction, cam_width - self.frame_reduction),
            (0, self.screen_width)
        )

        y3 = np.interp(
            y,
            (self.frame_reduction, cam_height - self.frame_reduction),
            (0, self.screen_height)
        )

        curr_x = self.prev_x + (x3 - self.prev_x) / self.smoothening
        curr_y = self.prev_y + (y3 - self.prev_y) / self.smoothening

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x = curr_x
        self.prev_y = curr_y

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def double_click(self):
        pyautogui.doubleClick()

    def drag_start(self):
        pyautogui.mouseDown()

    def drag_stop(self):
        pyautogui.mouseUp()