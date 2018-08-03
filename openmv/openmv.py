from io import BytesIO

import serial

from openmv import image_reader
from stream_handler import StreamHandler


class OpenMVStreamHandler(StreamHandler):
    # Connects to the OpenMV camera via serial.
    try:
        camera = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=None)
    except Exception as e:
        print("Could not connect to the OpenMV camera.")
        print(e)

    def get_frame(self):
        # Gets the image from the OpenMV camera.
        img = image_reader.get_frame(self.camera)
        # Saves the image to a bytes buffer.
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        # Gets the value stored in the buffer.
        frame = buffer.getvalue()
        return frame
