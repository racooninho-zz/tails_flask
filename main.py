# External imports
import tornado.ioloop
import tornado.web
import web

tornado_routes = [
    (r"/order", web.Order)]


def main():
    application = tornado.web.Application([
        (r"/order", web.Order)
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    
 
if __name__ == "__main__":
    main()
 
