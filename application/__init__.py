# importing required packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create application
app = Flask(__name__)

# set application configuration
app.config['SECRET_KEY'] = 'lx7E6161UpH9zwYlg1Mh38kljs987PO6do58OKca'
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_PATH'] = 2048

# define db
db = SQLAlchemy(app)

# import routes
from application import routes
