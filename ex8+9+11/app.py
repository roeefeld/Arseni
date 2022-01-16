from flask import Flask  ,render_template, request,session ,blueprints
import  mysql, mysql.connector
import requests
from  flask import  jsonify

app = Flask(__name__)
app.secret_key = '123'

users = {"user1": {"UserName": "erani","First Name": "Eran","Last Name": "Zehavi", "Email": "eranosh@gmail.com"},
         "user2": {"UserName": "dori","First Name": "Dor", "Last Name": "micha", "Email": "dordor@gmail.com"},
         "user3": {"UserName": "tali","First Name": "Tal", "Last Name": "Ben-Haim", "Email": "talben@gmail.com"},
         "user4": {"UserName": "ori","First Name": "Ori", "Last Name": "malmilian", "Email": "malmil@gmail.com"},
         "user5": {"UserName": "Ayelet", "First Name": "Ayelet", "Last Name": "Shaked", "Email": "ayeletsha@gmail.com"}
         }

from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


##################### Arseni's function ##################################
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='ex10Roee')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value

# EX-11

@app.route('/assignment11/users', methods=['GET', 'POST'])
def assignment11_return():

    usersTable = interact_db(query="select * from ex10Roee.users", query_type='fetch')
    ans = {}
    i = 0
    print(9999999)

    for user in usersTable:
        i += 1
        user = {
            'user': user.userName,
            'first name': user.firstName,
            'last name': user.lastName,
            'email': user.email,
        }
        ans[f'user{i}'] = user
    return jsonify(ans)


@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def outer_source():
    if "id" in request.args:
        if request.args['id'] == '':
            return render_template('assignment11.html', user = -1)
        id = int(request.args['id'])
        res = requests.get(f'https://reqres.in/api/users/{id}')
        user = res.json()
        return render_template('assignment11.html', user= user)
    else:
        return render_template('assignment11.html', user=-1)



#------------------------

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

@app.route('/assignment12/restapi_users', defaults={'user_id': -1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_user_func(user_id):
    if user_id == -1:
       user_id = random.randrange(1, len(users))
    ret = {}
    query = "select * from users WHERE id='%s';" % user_id
    userss = interact_db(query=query, query_type='fetch')
    if len(userss) == 0:
        ret = {
            'status': 'failed',
            'message': 'no user'
        }
    else:
        for user in userss:
            ret[f'user_{user.id}'] = {
                'status': 'succeed',
                'First Name': user.firstName,
                'User Name': user.userName,
                'Last Name': user.lastName,
                'Email': user.email,
            }
    return jsonify(ret)

if __name__ == '__main__':
    app.run(debug=True)