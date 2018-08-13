import time
from io import BytesIO
from threading import Condition

import picamera

from stream_handler import StreamHandler


class StreamingOutput:
    def __init__(self):
        self.frame = None
        self.buffer = BytesIO()
        self.condition = Condition()

    def write(self, buffer):
        if buffer.startswith(b"\xff\xd8"):
            # New frame, copy the existing buffer's content and notify all clients it's available.
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buffer)


class InfraredStreamHandler(StreamHandler):
    try:
        from picamera import PiCamera
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 30
        # Allow time for the camera to warm up.
        time.sleep(2)
        # Begin recording.
        output = StreamingOutput()
        camera.start_recording(output, format="mjpeg")
    except Exception as e:
        print("Could not connect to the infrared camera.")
        print(e)

    @classmethod
    def get_frame(cls):
        with cls.output.condition:
            cls.output.condition.wait()
            frame = cls.output.frame
            return frame
