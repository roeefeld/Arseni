from flask import Flask  ,render_template, request,session

app = Flask(__name__)
app.secret_key = '123'
users = {"user1": {"UserName": "erani","First Name": "Eran","Last Name": "Zehavi", "Email": "eranosh@gmail.com"},
         "user2": {"UserName": "dori","First Name": "Dor", "Last Name": "micha", "Email": "dordor@gmail.com"},
         "user3": {"UserName": "tali","First Name": "Tal", "Last Name": "Ben-Haim", "Email": "talben@gmail.com"},
         "user4": {"UserName": "ori","First Name": "Ori", "Last Name": "malmilian", "Email": "malmil@gmail.com"},
         "user5": {"UserName": "Ayelet", "First Name": "Ayelet", "Last Name": "Shaked", "Email": "ayeletsha@gmail.com"}
         }



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


@app.route('/assignment9' , methods = ['GET','POST'])
def assignment9():
    current_method = request.method
    if current_method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name is '':
                return render_template('assignment9.html', search=True, users=users, find=True)
            user_dic = {}
            for user in users.values():
                if user['UserName'] == user_name:
                    user_dic[1] = user
            if len(user_dic) != 0:
                return render_template('assignment9.html', search=True, find=True, users=user_dic)
            else:
                return render_template('assignment9.html', find=False, search=True)
        return render_template('assignment9.html')
    elif current_method == 'POST':
        session['login'] = True
        users[request.form['email']] = {'First Name': request.form['firstName'],
                                            'Last Name': request.form['lastName'],
                                            'Email': request.form['email'],
                                            'User Name': request.form['userName']}
        session['userName'] = request.form['userName']
        return render_template('assignment9.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['login'] = False
    return render_template('CVgrid.html')



if __name__ == '__main__':
    app.run()