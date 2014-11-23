from flask import Flask
from flask import make_response
from flask import redirect
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello dipper!'

@application.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

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
