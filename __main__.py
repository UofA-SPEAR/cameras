import tornado.ioloop
import tornado.web

import infrared.infrared
import openmv.openmv
import webcam.webcam


def main():
    app = tornado.web.Application([
        (r"/stream/openmv", openmv.openmv.OpenMVStreamHandler),
        #(r"/stream/webcam", webcam.webcam.WebcamStreamHandler),
        #(r"/stream/infrared", infrared.infrared.InfraredStreamHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
