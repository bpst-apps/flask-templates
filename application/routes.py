# importing required packages
import os.path
import sqlite3 as sql
from application import app, db
from flask import render_template, request, url_for, redirect, flash
from werkzeug.utils import secure_filename
from application.models import Student


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
        return render_template("result.html", result=result, title='Flask Templates')


# ***************************************** URL ROUTING END ************************************************************
# **********************************************************************************************************************
# ***************************************** FILE UPLOAD START **********************************************************
# hit this uri: http://127.0.0.1:5000/upload
@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def file_uploader():
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.mkdir(app.config['UPLOAD_FOLDER'])
        f.save(app.config['UPLOAD_FOLDER'] + '/' + secure_filename(f.filename))
        return 'file uploaded successfully'


# ***************************************** FILE UPLOAD END ************************************************************
# **********************************************************************************************************************
# ***************************************** SQLITE3 START **************************************************************
# hit this uri: http://127.0.0.1:5000/new-student
@app.route('/new-student')
def new_student():
    return render_template('new-student.html')


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("app-database.db") as con:
                cur = con.cursor()
                create_table_query = """CREATE TABLE IF NOT EXISTS STUDENTS(
                    RECORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT NOT NULL,
                    ADDRESS TEXT NOT NULL,
                    CITY TEXT NOT NULL,
                    PIN TEXT NOT NULL
                );"""
                cur.execute(create_table_query)
                cur.execute("INSERT INTO STUDENTS (NAME, ADDRESS, CITY, PIN) VALUES(?, ?, ?, ?)",
                            (name, address, city, pin))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("new-student-result.html", msg=msg, title='Flask Templates')
            con.close()


# hit this uri: http://127.0.0.1:5000/list-students
@app.route('/list-students')
def list_students():
    con = sql.connect("app-database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM STUDENTS")

    rows = cur.fetchall()
    return render_template("students-list.html", rows=rows, title='Flask Templates')


# ***************************************** SQLITE3 END ****************************************************************
# **********************************************************************************************************************
# ***************************************** SQLALCHEMY START ***********************************************************
# hit this uri: http://127.0.0.1:5000/show-all
@app.route('/show-all')
def show_all():
    return render_template('show_all.html', students=Student.query.all())


# hit this uri: http://127.0.0.1:5000/add-new-student
@app.route('/add-new-student', methods=['GET', 'POST'])
def new_student_to_db():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['address']:
            flash('Please enter all the fields', 'error')
        else:
            student = Student(request.form['name'], request.form['city'],
                              request.form['address'], request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')
# ***************************************** SQLALCHEMY END *************************************************************
