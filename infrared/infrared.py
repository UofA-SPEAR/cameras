import time
from io import BytesIO

from stream_handler import StreamHandler


class InfraredStreamHandler(StreamHandler):
    def __init__(self, application, request):
        try:
            from picamera import PiCamera
            self.camera = PiCamera()
            self.camera.resolution = (640, 480)
            self.camera.framerate = 80
            # Allow time for the camera to warm up.
            time.sleep(2)
        except Exception as e:
            print("Could not connect to the infrared camera.")
            print(e)
        super().__init__(application, request)

    def get_frame(self):
        stream = BytesIO()
        self.camera.capture(stream, format="jpeg", quality=35)
        frame = stream.getvalue()
        return frame
