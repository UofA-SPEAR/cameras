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


class WebcamStreamHandler(StreamHandler):
    try:
        pygame.camera.init()
        cameras = pygame.camera.list_cameras()
        self.camera = pygame.camera.Camera(cameras[0], IMAGE_SIZE)
        self.camera.start()
    except Exception as e:
        print("Could not connect to the webcam.")
        print(e)

    def get_frame(self):
        img = self.camera.get_image()
        img = pygame.image.tostring(img, "RGB", False)
        img = Image.frombytes("RGB", IMAGE_SIZE, img)
        # Saves the image to a bytes buffer.
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        # Gets the value stored in the buffer.
        frame = buffer.getvalue()
        return frame
