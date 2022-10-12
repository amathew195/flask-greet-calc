from flask import Flask

app = Flask(__name__)


@app.get('/welcome')
def say_welcome():
    html = "<p>Welcome</p>"
    return html


@app.get('/welcome/home')
def say_welcome_home():
    html = "<p>Welcome home</p>"
    return html


@app.get('/welcome/back')
def say_welcome_back():
    html = "<p>Welcome back</p>"
    return html
