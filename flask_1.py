from flask import Flask, render_template, request
from werkzeug.utils import redirect
import pymysql
from api import searchapi
from datetime import datetime
from db_reg import indb, outdb
import api_test
import api_test1

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/favorite')
def favorite():
    return render_template('jmy.html')


@app.route('/regester')
def regester():
    return render_template('regester.html')

@app.route('/save_reg', methods=['GET','POST'])
def save_reg():
    username = request.form['username']
    email = request.form['email']
    data = [
        (username, email),
    ]
    indb(data)
    return render_template('index.html')

@app.route('/show_reg', methods=['GET','POST'])
def show_reg():
    sql_search_code = """
                        select * from user_info
                    """
    username=outdb(sql_search_code)

    return render_template('save_reg.html',
                           the_name=username)

@app.route('/management')
def management():
    return render_template('dash.html')

@app.route('/login')
def sign():
    return render_template('sign-in.html')

@app.route('/person')
def person():
    return render_template('person.html')

@app.route('/ManagementExit')
def dashboardExit_page() -> 'html':
    return render_template('index.html')

def log_request(req:'flask_request', res:str) -> None:
    with open('vsearch.log','a+', encoding='utf-8') as log:
        phrase = request.form['phrase']
        searchr = api_test1.searchapi(phrase)
        now_time=datetime.now()
        new_time=now_time.strftime('%Y-%m-%d %H:%M:%S')
        print("{}|{}|{}".format(res, new_time,searchr))
        log.write("{}|{}|{}\n".format(res, new_time,searchr))

@app.route('/results', methods=['GET','POST'])
def do_search():
    phrase = request.form['phrase']

    if phrase:
        log_request(request,phrase)
        searchresult = api_test.searchapi(phrase)
        searchr = api_test1.searchapi(phrase)
    if(searchr=='有害垃圾'):
        return render_template('2.html',searchresult = searchresult,p=phrase)
    if(searchr=='可回收物'):
        return render_template('1.html',searchresult = searchresult,p=phrase)
    if(searchr=='干垃圾'):
        return render_template('4.html', searchresult=searchresult, p=phrase)
    if(searchr=='湿垃圾'):
        return render_template('3.html', searchresult=searchresult, p=phrase)
    if(searchr=='暂时无法查询到该垃圾的分类结果，有待我们完善'):
        return render_template('error.html', searchresult=searchresult, p=phrase)

@app.route('/')
def entry_page():
    return render_template('index.html')

@app.route('/history')
def view_the_log():
    contents = []
    try:
        with open('vsearch.log','r', encoding='utf-8') as log:
            for line in log:
                content = [i for i in line.split('|')]
                contents.append(content)
        print(contents)

    except Exception as e:
        print(e)

    return render_template('admin.html',
                           the_title='View log',
                           the_data = contents)
if __name__ == '__main__':
     app.run(debug=True,host='172.17.0.6',port='80')
