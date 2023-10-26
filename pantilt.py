import pantilthat
import time


def reset():
    pantilthat.tilt(0)
    pantilthat.pan(0)

def move(rotation_type: str, rotation_direction: int):
    PAN = 0
    TILT = 0
    SPEED = 5

    movement = rotation_direction * SPEED
    if rotation_type == 'tilt':
        TILT = TILT + movement
        pantilthat.tilt(TILT)
        time.sleep(0.1)
    else:
        PAN = PAN + movement
        pantilthat.pan(PAN)
        time.sleep(0.01)