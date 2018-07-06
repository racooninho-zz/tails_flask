# External imports
import tornado.ioloop
import tornado.web
import web
import os
tornado_routes = [
    (r"/order", web.Order)]

 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.re("To test the API, go to /order/ and POST:\n "
                   """{
	"order": {
		"id": 12345,
		"currency": "USD",
		"customer": {

		},
		"items": [
			{
				"product_id": 1,
				"quantity": 1
			},
			{
				"product_id": 2,
				"quantity": 5
			},
			{
				"product_id": 3,
				"quantity": 1
			}
		]
	}
}""")

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
 
