import sys

import tornado.ioloop
import tornado.web

from image_handler import ImageHandler


def main():
    if len(sys.argv) < 2:
        print("Not enough arguments supplied.", file=sys.stderr)
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments supplied.", file=sys.stderr)
        sys.exit(1)

    device = sys.argv[1]
    if device == "rpi":
        from infrared.infrared import InfraredStreamHandler
        app = tornado.web.Application([
            (r"/stream/infrared", InfraredStreamHandler),
            (r"/image/infrared", ImageHandler)
        ])
    elif device == "tx2":
        from openmv.openmv import OpenMVStreamHandler
        from webcam.webcam import WebcamStreamHandler
        from webcam2.webcam2 import Webcam2StreamHandler
        app = tornado.web.Application([
            (r"/stream/openmv", OpenMVStreamHandler),
            (r"/image/openmv", ImageHandler),

            (r"/stream/webcam", WebcamStreamHandler),
            (r"/image/webcam", ImageHandler),

            (r"/stream/webcam2", Webcam2StreamHandler),
            (r"/image/webcam2", ImageHandler),
        ])
    else:
        print("Invalid argument. Please choose either rpi or tx2.", file=sys.stderr)
        sys.exit(1)

    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
