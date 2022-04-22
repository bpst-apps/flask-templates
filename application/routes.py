# importing required packages
from application import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome', username='Admin')


# hit this uri: http://127.0.0.1:5000/if-else-example
@app.route('/if-else-example')
def if_else_example():
    username = 'Bhanu Singh'  # change this and see magic working :)
    return render_template('if-else-example.html', title='Welcome', username=username)


# hit this uri: http://127.0.0.1:5000/for-loop-example
@app.route('/for-loop-example')
def for_loop_example():
    users = ['Bhanu Singh', 'Rohan Menon', ' John Mathew', 'Imran Khan', 'Varun Jain']
    return render_template('for-loop-example.html', title='Welcome', members=users)


# hit this url: http://127.0.0.1:5000/user/ron
@app.route('/user/<name>')
def view_user(name):
    return render_template('route-parameter-example.html', title='Welcome', username=str(name))


# hit this url: http://127.0.0.1:5000/user/bhanu/singh
@app.route('/user/<first_name>/<last_name>')
def view_user_full(first_name=None, last_name=None):
    return render_template('multiple-route-parameter-example.html', title='Welcome',
                           lastname=str(last_name), firstname=first_name)
