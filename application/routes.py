# importing required packages
from application import app
from flask import render_template, request, url_for, redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Flask Templates', username='Admin')


# hit this uri: http://127.0.0.1:5000/if-else-example
@app.route('/if-else-example')
def if_else_example():
    username = 'Bhanu Singh'  # change this and see magic working :)
    return render_template('if-else-example.html', title='Flask Templates', username=username)


# hit this uri: http://127.0.0.1:5000/for-loop-example
@app.route('/for-loop-example')
def for_loop_example():
    users = ['Bhanu Singh', 'Rohan Menon', ' John Mathew', 'Imran Khan', 'Varun Jain']
    return render_template('for-loop-example.html', title='Flask Templates', members=users)


# hit this url: http://127.0.0.1:5000/user/ron
@app.route('/user/<name>')
def view_user(name):
    return render_template('route-parameter-example.html', title='Flask Templates', username=str(name))


# hit this url: http://127.0.0.1:5000/user/bhanu/singh
@app.route('/user/<first_name>/<last_name>')
def view_user_full(first_name=None, last_name=None):
    return render_template('multiple-route-parameter-example.html', title='Flask Templates',
                           lastname=str(last_name), firstname=first_name)


# ***************************************** POST METHOD START **********************************************************
# hit this url: http://127.0.0.1:5000/login
@app.route('/dashboard/<name>')
def dashboard(name):
    return render_template('index.html', title='Flask Templates', username=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('dashboard', name=user))
    else:
        user = request.args.get('name')
        return render_template('login.html')


# ***************************************** POST METHOD END ************************************************************
# **********************************************************************************************************************
# ***************************************** JS INTEGRATION START *******************************************************
# hit this uri: http://127.0.0.1:5000/js-integration-example
@app.route('/js-integration-example')
def js_integration_example():
    return render_template('js-integration-example.html', title='Flask Templates')


# ***************************************** JS INTEGRATION END *********************************************************
# **********************************************************************************************************************
# ***************************************** URL ROUTING START **********************************************************
# hit this uri: http://127.0.0.1:5000/student
@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)
# ***************************************** URL ROUTING END ************************************************************
