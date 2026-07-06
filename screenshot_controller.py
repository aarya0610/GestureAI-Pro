import pyautogui
from datetime import datetime
import os


class ScreenshotController:

    def __init__(self):
        self.folder = "Screenshots"

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def take_screenshot(self):

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

        path = os.path.join(self.folder, filename)

        image = pyautogui.screenshot()

        image.save(path)

        return path