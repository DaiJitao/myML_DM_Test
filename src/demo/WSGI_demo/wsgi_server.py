#coding:utf-8
from wsgiref.simple_server import make_server
import demo.WSGI_demo.webapp as web_application

server = make_server('', 8899, web_application.application)
server.serve_forever()

