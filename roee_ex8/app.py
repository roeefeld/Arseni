from flask import Flask,url_for, redirect ,render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def main():
    return render_template('CVgrid.html')

@app.route('/exercise2')
def exercise2():
    return render_template('exercise2.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/assignment8')
def assignment8():
    maccabi = ("eran zeHavi", "dor micha", "tal ben haim", "ori malmilian")
    return render_template('assignment8.html', maccabi = maccabi)



if __name__ == '__main__':
    app.run()