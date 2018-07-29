from io import BytesIO

import cv2
from PIL import Image

import streamer.streamer


class WebcamStreamHandler(streamer.streamer.StreamHandler):
    def __init__(self, application, request):
        try:
            self.camera = cv2.VideoCapture(0)
        except Exception:
            print("Could not connect to the webcam.")
        super(WebcamStreamHandler, self).__init__(application, request)

    def get_frame(self):
        _, img = self.camera.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        # Saves the image to a bytes buffer.
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        # Gets the value stored in the buffer.
        frame = buffer.getvalue()
        return frame
