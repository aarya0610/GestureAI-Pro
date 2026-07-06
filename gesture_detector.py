import cv2
import mediapipe as mp


class GestureDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb)

        fingers = 0
        gesture = "No Hand"
        index_x = 0
        index_y = 0
        thumb_x = 0
        thumb_y = 0

        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]

            self.mp_draw.draw_landmarks(
                frame,
                hand,
                self.mp_hands.HAND_CONNECTIONS
            )

            tips = [4, 8, 12, 16, 20]
            index_x = hand.landmark[8].x
            index_y = hand.landmark[8].y
            thumb_x = hand.landmark[4].x
            thumb_y = hand.landmark[4].y

            # Thumb
            if hand.landmark[4].x < hand.landmark[3].x:
                fingers += 1

            # Other fingers
            for tip in tips[1:]:
                if hand.landmark[tip].y < hand.landmark[tip - 2].y:
                    fingers += 1

            names = {
                0: "Fist",
                1: "One Finger",
                2: "Two Fingers",
                3: "Three Fingers",
                4: "Four Fingers",
                5: "Open Palm"
            }

            gesture = names.get(fingers, "Unknown")

        return (
    frame,
    fingers,
    gesture,
    index_x,
    index_y,
    thumb_x,
    thumb_y
)