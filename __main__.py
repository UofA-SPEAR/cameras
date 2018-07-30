import sys

import tornado.ioloop
import tornado.web

import infrared.infrared
import openmv.openmv
import webcam.webcam


def main():
    if len(sys.argv) != 2:
        raise ValueError("Please specify the device as a command line argument: rpi or tx2.")

    device = sys.argv[1]
    if device == "rpi":
        app = tornado.web.Application([
            (r"/stream/infrared", infrared.infrared.InfraredStreamHandler)
        ])
    elif device == "tx2":
        app = tornado.web.Application([
            (r"/stream/openmv", openmv.openmv.OpenMVStreamHandler),
            (r"/stream/webcam", webcam.webcam.WebcamStreamHandler),
        ])
    else:
        raise ValueError("Second argument must be either rpi or tx2.")

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
