# -*- coding: UTF-8 -*-

'''
返回相应的数据
'''
import web

def get_json_questions():
    DB = web.database(dbn='mysql', db='pufa', user='root', pw='')
    results = DB.query('SELECT id, a_answer, b_answer, c_answer, d_answer, content FROM questions ORDER BY rand() LIMIT 5')
    res = []
    for item in results:
        tmp_json = {}
        tmp_json['id'] = item['id']
        tmp_json['1'] = item['a_answer']
        tmp_json['2'] = item['b_answer']
        tmp_json['3'] = item['c_answer']
        tmp_json['4'] = item['d_answer']
        tmp_json['title'] = item['content']
        res.append(tmp_json)
    return {'results':res}

def check(id, choice_user):
    DB = web.database(dbn='mysql', db='pufa', user='root', pw='')
    results = DB.query("SELECT correct_answer FROM questions WHERE id = '"+str(id)+"'")
    if len(results) == 0:
        return False
    elif str(results[0]['correct_answer']).lower().strip() == str(choice_user).lower().strip():
        return True
    else:
        return False

def record(name, phone_num, grade):
    DB = web.database(dbn='mysql', db='pufa', user='root', pw='')
    try:
        results = DB.query("INSERT INTO records (phone_number, name, grade) VALUES ('"+str(phone_num)+"', '"+str(name).encode('utf8')+"', '"+str(grade)+"')")
        return True
    except:
        return False

