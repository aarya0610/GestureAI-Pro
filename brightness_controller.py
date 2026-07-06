import screen_brightness_control as sbc

def set_brightness(percent):

    percent = max(0, min(100, percent))

    sbc.set_brightness(percent)