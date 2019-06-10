#coding:utf-8
from wsgiref.simple_server import make_server
import src.demo.WSGI_demo.webapp as web_application

httpd = make_server('', 8899, web_application.application)  # 生成服务

print("Serving HTTP on port 8899...")

httpd.serve_forever()

