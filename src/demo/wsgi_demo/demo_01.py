#coding:utf-8

from wsgiref.simple_server import make_server

def demo_app(env, start_response):
    from StringIO import StringIO
    print >> stout, ""