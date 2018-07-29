import time
from io import BytesIO

import streamer.streamer


class InfraredStreamHandler(streamer.streamer.StreamHandler):
    def __init__(self, application, request):
        try:
            from picamera import PiCamera
            self.camera = PiCamera()
            self.camera.resolution = (640, 480)
            self.camera.framerate = 80
            self.camera.start_preview()
            # Allow time for the camera to warm up.
            time.sleep(2)
        except Exception:
            print("Could not connect to the infrared camera.")
        super(InfraredStreamHandler, self).__init__(application, request)

    def get_frame(self):
        stream = BytesIO()
        self.camera.capture(stream, format="jpeg", quality=35)
        frame = stream.getvalue()
        return frame
