from flask import Flask, render_template, request
from werkzeug.utils import redirect
import pymysql
from api import searchapi
from db_reg import indb

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
    return render_template('save_reg.html',
                           the_name=username,
                           the_email=email)

@app.route('/admin')
def admin():
    return render_template('dash.html')

app.run(debug=True)
