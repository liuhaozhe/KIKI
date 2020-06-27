from flask import Flask, render_template, request
from werkzeug.utils import redirect
import pymysql
from api import searchapi
from db_reg import indb, outdb

app = Flask(__name__)

@app.route('/results', methods=['GET','POST'])
def do_search():
    phrase = request.form['phrase']
    if phrase:
        searchresult = searchapi(phrase)
    return render_template('results.html',
                           the_search=phrase,
                           the_result=searchresult)

@app.route('/')
def start():
    return render_template('index.html')


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

@app.route('/admin')
def admin():
    return render_template('dash.html')

app.run(debug=True)
