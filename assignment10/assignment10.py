from flask import Flask, render_template, session, request, redirect, Blueprint , flash
import mysql , mysql.connector

app = Flask(__name__)
app.secret_key = "123"


assignment10 = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/assignment10',
    template_folder='templates'
)


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


@assignment10.route('/assignment10')
def users():
    usersTable = interact_db(query="select * from ex10Roee.users", query_type='fetch')
    if session.get('messages'):
        x = session['messages']
        session.pop('messages')
        return render_template('assignment10.html', users=usersTable, messages = x)
    else:
        return render_template('assignment10.html', users=usersTable)



@assignment10.route('/insertUser', methods=['GET','POST'])
def insertUsers():
    if request.method == 'POST':
        userName = request.form['firstName']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        check_input = "SELECT userName FROM ex10Roee.users WHERE userName='%s';" % userName
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into ex10Roee.users(userName, firstName ,lastName, email)\
                            value ('%s', '%s', '%s','%s');" % (userName,firstName ,lastName, email)
            interact_db(query=query, query_type='commit')
            flash('user added!!! ')
            return redirect('/assignment10')
        else:
            flash('the user name is taken, please try another name')
            return redirect('/assignment10')
    return render_template('assignment10.html', req_method=request.method)



@assignment10.route('/deleteUser', methods=['POST'])
def deleteUsers():
    userName = request.form['userName']
    check = "SELECT userName FROM ex10Roee.users WHERE userName='%s';" % userName
    answer = interact_db(query=check, query_type='fetch')
    if len(answer) > 0:
        query = "delete from ex10Roee.users where userName='%s';" % userName
        interact_db(query=query, query_type='commit')
        flash('user deleted ')
        return redirect('/assignment10')
    else:
        flash('the user you are trying to delete does not exist')
        return redirect('/assignment10')


@assignment10.route('/updateUser', methods=['GET','POST'])
def updateUsers():
        username = request.form['userName']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        email = request.form['email']
        query = " UPDATE ex10Roee.users SET firstName='%s' ,lastName='%s', email='%s' WHERE userName='%s';"%\
                (firstname, lastname, email,username)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
