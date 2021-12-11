from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/')
def main():
    return 'welcome to web course'


@app.route('/about')
def about1():
    return 'Welcome to my page'


@app.route('/info')
def info():
 return redirect('/about')


@app.route('/payment')
def errorpage():
 return redirect(url_for('main'))


if __name__ == '__main__':
    app.run()
