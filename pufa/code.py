# -*- coding: UTF-8 -*-

import web
import json

import db

urls = (
    '/', 'index',
    '/get_questions', 'question',
    '/verify_choices', 'verify'
)

class index:
    def GET(self):
        raise web.seeother('/static/app.html')

class question:
    def GET(self):
        web.header('content-type','text/json')
        return json.dumps(db.get_json_questions())
        # return json.dumps({'results':[{'id':1,'title':'title01','1':'Aaaaa','2':'bbbb','3':'ccc','4':'dddd'},
        #                               {'id':2, 'title': 'title02', '1': 'aaaaa', '2': 'Bbbb', '3': 'ccc', '4': 'dddd'},
        #                               {'id':3, 'title': 'title03', '1': 'aaaaa', '2': 'bbbb', '3': 'Ccc', '4': 'dddd'},
        #                               {'id':4, 'title': 'title04', '1': 'aaaaa', '2': 'bbbb', '3': 'ccc', '4': 'Dddd'},
        #                               {'id':5, 'title': 'title05', '1': 'aaaaa', '2': 'bbbb', '3': 'ccc', '4': 'ddDd'},]})

class verify:
    def GET(self):
        user_data = web.input()
        phone_num = user_data['phone_num']
        name = user_data['name']
        choices = eval(user_data['choices'])

        # web.header('content-type', 'json')
        # return json.dumps({'correct_num': name, 'error':'yes'})

        flag = True
        count = 0
        for k, v in choices.iteritems():
            try:
                if db.check(k, v):
                    count +=1
            except:
                flag = False
                break
        if flag:
            if db.record(name,phone_num,count):
                web.header('content-type','json')
                return json.dumps({'correct_num':count, 'error':'no'})
            else:
                web.header('content-type', 'json')
                return json.dumps({'correct_num': 0, 'error': 'yes'})
        else:
            web.header('content-type', 'json')
            return json.dumps({'correct_num': 0, 'error':'yes'})

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()