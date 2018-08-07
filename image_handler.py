import tornado.gen
import tornado.ioloop
import tornado.web


class ImageHandler(tornado.web.RequestHandler):
    def get(self):
        camera_name = self.request.uri.split("/")[-1]

        if camera_name == "infrared":
            from infrared.infrared import InfraredStreamHandler
            stream_handler = InfraredStreamHandler
        elif camera_name == "openmv":
            from openmv.openmv import OpenMVStreamHandler
            stream_handler = OpenMVStreamHandler
        elif camera_name == "webcam":
            from webcam.webcam import WebcamStreamHandler
            stream_handler = WebcamStreamHandler
        else:
            raise tornado.web.HTTPError(404)

        # Disables CORS.
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")

        # Prevents caching.
        self.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.set_header("Pragma", "no-cache")
        self.set_header("Expires", "0")

        frame = stream_handler.get_frame()
        # Writes the necessary headers.
        self.set_header("Content-Type", "image/jpeg")
        self.set_header("Content-Length", str(len(frame)))

        # Writes the image.
        self.write(frame)
