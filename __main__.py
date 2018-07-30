import sys

import tornado.ioloop
import tornado.web

from infrared.infrared import InfraredStreamHandler
from openmv.openmv import OpenMVStreamHandler
from webcam.webcam import WebcamStreamHandler


def main():
    if len(sys.argv) != 2:
        raise ValueError("Please specify the device as a command line argument. Options are rpi and tx2.")

    device = sys.argv[1]
    if device == "rpi":
        app = tornado.web.Application([
            (r"/stream/infrared", InfraredStreamHandler)
        ])
    elif device == "tx2":
        app = tornado.web.Application([
            (r"/stream/openmv", OpenMVStreamHandler),
            (r"/stream/webcam", WebcamStreamHandler),
        ])
    else:
        raise ValueError("Second argument must be either rpi or tx2.")

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
