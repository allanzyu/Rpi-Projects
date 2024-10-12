from picamera2 import Picamera2, Preview
import time

camera = Picamera2()
time.sleep(5)
camera.capture_file("test.jpg")
#test comment
