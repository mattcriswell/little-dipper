from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
application = Flask(__name__)

months = [ 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec' ]
test = "hello test"

@application.route('/')
def hello_world():
    return render_template('index.html')

@application.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@application.route('/cookie')
def cookiemonster():
    response = make_response('<h1>This document carries a cookie.</h1>')
    response.set_cookie('answer', '42')
    return response

@application.route('/charts/<name>')
def charts(name):
    return render_template('charts.html', name=name, months=months, test=test)

@application.route('/google')
def google():
    return redirect('https://www.google.com')

if __name__ == '__main__':
    app.run()

#hamburgers
