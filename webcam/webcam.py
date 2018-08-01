from io import BytesIO

import pygame
import pygame.camera
import pygame.image
from PIL import Image

from stream_handler import StreamHandler


class WebcamStreamHandler(StreamHandler):
    def __init__(self, application, request):
        try:
            pygame.camera.init()
            cameras = pygame.camera.list_cameras()
            self.camera = pygame.camera.Camera(cameras[0])
            self.camera.start()
        except Exception as e:
            print("Could not connect to the webcam.")
            print(e)
        super().__init__(application, request)

    def get_frame(self):
        img = self.camera.get_image()
        img = pygame.image.tostring(img, "RGBA", False)
        img = Image.frombytes("RGBA", img)
        # Saves the image to a bytes buffer.
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        # Gets the value stored in the buffer.
        frame = buffer.getvalue()
        return frame
