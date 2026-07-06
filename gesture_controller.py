import math


class GestureController:

    def __init__(self):
        self.tipIds = [4, 8, 12, 16, 20]

    def fingersUp(self, lmList):

        if len(lmList) == 0:
            return []

        fingers = []

        # Thumb
        if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
            fingers.append(0)
        else:
            fingers.append(1)

        # Index, Middle, Ring, Pinky
        for i in range(1, 5):
            if lmList[self.tipIds[i]][2] < lmList[self.tipIds[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def findDistance(self, p1, p2):

        x1, y1 = p1
        x2, y2 = p2

        length = math.hypot(x2 - x1, y2 - y1)

        return length

    def detectGesture(self, fingers):

        if fingers == [1, 0, 0, 0, 0]:
            return "GOOGLE"

        elif fingers == [0, 1, 0, 0, 0]:
            return "MOUSE"

        elif fingers == [0, 1, 1, 0, 0]:
            return "LEFT_CLICK"

        elif fingers == [1, 1, 0, 0, 0]:
            return "RIGHT_CLICK"

        elif fingers == [1, 1, 1, 0, 0]:
            return "DOUBLE_CLICK"

        elif fingers == [0, 1, 1, 1, 0]:
            return "YOUTUBE"

        elif fingers == [1, 1, 1, 1, 1]:
            return "CHATGPT"

        elif fingers == [1, 0, 0, 0, 1]:
            return "GITHUB"

        elif fingers == [1, 1, 0, 0, 1]:
            return "LINKEDIN"

        elif fingers == [0, 0, 0, 0, 0]:
            return "DRAG"
        
        elif fingers == [1, 0, 1, 0, 0]:
            return "CALCULATOR"

        elif fingers == [1, 0, 1, 1, 0]:
            return "NOTEPAD"

        elif fingers == [1, 0, 1, 1, 1]:
            return "EXPLORER"

        elif fingers == [0, 0, 1, 1, 1]:
            return "PAINT"
        
        elif fingers == [0, 0, 0, 1, 1]:
            return "SCREENSHOT"
        
        elif fingers == [0, 0, 1, 0, 0]:
            return "SCROLL"

        # -----------------------------
        # Volume Mode
        # -----------------------------
        elif fingers == [1, 1, 0, 1, 0]:
            return "VOLUME"
        
        # -----------------------------
        # Brightness Control
        # -----------------------------
        elif fingers == [1, 0, 1, 0, 1]:
            return "BRIGHTNESS"
        
        elif fingers == [0, 0, 1, 0, 1]:
            return "DRAW"
        
        # -----------------------------
        # Media Controls
        # -----------------------------
        elif fingers == [0, 1, 0, 1, 1]:
           return "PLAY_PAUSE"

        elif fingers == [0, 1, 0, 0, 1]:
           return "NEXT_TRACK"

        elif fingers == [1, 1, 1, 1, 0]:
           return "PREVIOUS_TRACK"
        
        else:
            return "NONE"