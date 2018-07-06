# External imports
import tornado.ioloop
import tornado.web
import web
import os
tornado_routes = [
    (r"/order", web.Order)]

 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("template.html")


def main():
    application = tornado.web.Application([
        (r"/order", web.Order),
        (r"/", MainHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
 
if __name__ == "__main__":
    main()
 
