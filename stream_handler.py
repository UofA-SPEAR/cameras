import tornado.gen
import tornado.ioloop
import tornado.web


class StreamHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # Prevents caching.
        self.set_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.set_header("Pragma", "no-cache")
        self.set_header("Expires", "0")
        # Closes the connection when lost.
        self.set_header("Connection", "close")
        # Specifies the resource is an MJPEG stream and the boundary to use.
        self.set_header("Content-Type", "multipart/x-mixed-replace;boundary=--boundarydonotcross")

        while True:
            frame = self.get_frame()
            # Writes the boundary between frames.
            self.write("--boundarydonotcross\n")
            # Writes the necessary headers.
            self.write("Content-Type: image/jpeg\r\n")
            self.write("Content-Length: {}\r\n\r\n".format(len(frame)))
            # Writes the image.
            self.write(frame)
            # Yields until the written data has been flushed.
            yield tornado.gen.Task(self.flush)

    @classmethod
    def get_frame(cls):
        raise NotImplementedError("Please override method get_frame.")
