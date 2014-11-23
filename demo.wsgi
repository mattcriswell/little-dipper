from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
application = Flask(__name__)

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

@application.route('/google')
def google():
    return redirect('https://www.google.com')

if __name__ == '__main__':
    app.run()

#hamburgers
