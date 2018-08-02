import sys

import tornado.ioloop
import tornado.web


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Not enough arguments supplied.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        sys.stderr.write("Too many arguments supplied.")
        sys.exit(1)

    device = sys.argv[1]
    if device == "rpi":
        from infrared.infrared import InfraredStreamHandler
        app = tornado.web.Application([
            (r"/stream/infrared", InfraredStreamHandler)
        ])
    elif device == "tx2":
        from openmv.openmv import OpenMVStreamHandler
        from webcam.webcam import WebcamStreamHandler
        app = tornado.web.Application([
            (r"/stream/openmv", OpenMVStreamHandler),
            (r"/stream/webcam", WebcamStreamHandler),
        ])
    else:
        sys.stderr.write("Invalid argument. Please choose either rpi or tx2.")
        sys.exit(1)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
