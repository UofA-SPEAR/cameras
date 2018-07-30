from io import BytesIO

import serial

from openmv import image_reader
from stream_handler import StreamHandler


class OpenMVStreamHandler(StreamHandler):
    def __init__(self, application, request):
        # Connects to the OpenMV camera via serial.
        try:
            self.camera = serial.Serial("COM11", baudrate=115200, timeout=None)
        except Exception:
            print("Could not connect to the OpenMV camera.")
        super(OpenMVStreamHandler, self).__init__(application, request)

    def get_frame(self):
        # Gets the image from the OpenMV camera.
        img = image_reader.get_frame(self.camera)
        # Saves the image to a bytes buffer.
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        # Gets the value stored in the buffer.
        frame = buffer.getvalue()
        return frame
