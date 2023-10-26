import pantilthat
import keyboard
import time


# from picamera2 import Picamera2, Preview

# picam = Picamera2()

# config = picam.create_preview_configuration()
# picam.configure(config)

# picam.start_preview(Preview.QTGL)

# picam.start()
# time.sleep(2)
# picam.capture_file("test-python.jpg")

# picam.close()


## Set angle for camera
# while True:  
#   pantilthat.pan(0)
#   pantilthat.tilt(-50)

PAN = 0
TILT = 0
SPEED = 1

def move(rotation_type: str, rotation_direction: int):
    movement = rotation_direction * SPEED
    if rotation_type == "tilt":
        TILT = TILT + movement
        pantilthat.tilt(TILT)
        time.sleep(0.1)
    else:
        PAN = PAN + movement
        pantilthat.pan(PAN)
        time.sleep(0.01)


while True:
    if keyboard.read_key() == "up":
        print('You pressed a up')
        move('tilt', -1)
    elif keyboard.read_key() == "down":
        print('You pressed down')
        move('tilt', 1)
    elif keyboard.read_key() == "left":
        print('You pressed left')
        move('pan', -1)
    elif keyboard.read_key() == "right":
        print('You pressed right')
        move('pan', 1)
