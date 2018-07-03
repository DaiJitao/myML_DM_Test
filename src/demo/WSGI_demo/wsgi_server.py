#coding:utf-8
from wsgiref.simple_server import make_server
import demo.WSGI_demo.webapp as web_application

httpd = make_server('', 8899, web_application.application)
print("Serving HTTP on port 8899...")
httpd.serve_forever()

