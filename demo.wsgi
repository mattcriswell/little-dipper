from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hello dipper!'

@application.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run()

#hamburgers
