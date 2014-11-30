from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
application = Flask(__name__)

months = [ 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec' ]
min_temp = [ 72, 74, 74, 69, 59, 49, 41 ]
max_temp = [ 91, 95, 95, 90, 82, 71, 64 ]

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

@application.route('/charts')
def charts():
    return render_template('charts.html', months=months, min_temp=min_temp, max_temp=max_temp)

@application.route('/google')
def google():
    return redirect('https://www.google.com')

if __name__ == '__main__':
    app.run()

#hamburgers
