#coding: utf-8

import web

urls = (
    '/', 'hello',
    '/questions', 'questions'
)

app = web.application(urls, globals[])

class hello:
    def GET(self):
        web.hander(('content-type', 'text/json'))
        return json.dumps({'id': 1, 'age': 23})

class questions:
    # get item
    def GET(self):
        return 'GET method'
    # add item
    def POST(self):
        return 'POST method'
    # update item
    def PUT(self):
        return 'PUT method'
    # delete item
    def DELETE(self):
        return 'DELETE method'

if True:
    app.run()