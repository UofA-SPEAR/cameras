import os
import sys
from io import BytesIO

# Suppress console output from pygame imports.
sys.stdout = open(os.devnull, "w")
import pygame
import pygame.camera
import pygame.image

# Restore console output.
sys.stdout = sys.__stdout__

from PIL import Image

from stream_handler import StreamHandler

IMAGE_SIZE = (640, 480)
#IMAGE_SIZE = (160, 120)


class Webcam2StreamHandler(StreamHandler):
    try:
        pygame.camera.init()
        cameras = pygame.camera.list_cameras()
        camera = pygame.camera.Camera(cameras[-2], IMAGE_SIZE)
        camera.start()
    except Exception as e:
        print("Could not connect to the webcam.")
        print(e)

    @classmethod
    def get_frame(cls):
        img = cls.camera.get_image()
        img = pygame.image.tostring(img, "RGB", False)
        img = Image.frombytes("RGB", IMAGE_SIZE, img).rotate(180)
        # Saves the image to a bytes buffer.
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        # Gets the value stored in the buffer.
        frame = buffer.getvalue()
        return frame
