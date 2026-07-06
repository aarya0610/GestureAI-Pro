import pyautogui

pyautogui.FAILSAFE = True


class ScrollController:

    def scroll_up(self):
        pyautogui.scroll(250)

    def scroll_down(self):
        pyautogui.scroll(-250)