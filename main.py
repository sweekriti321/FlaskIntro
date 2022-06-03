from flask import Flask,render_template
from flask_mysqldb import MySQL
app=Flask(__name__)

@app.route('/register')
def index():
    return render_template('register.html')

@app.route('/')
def elec():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


app.run()



