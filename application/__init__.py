# importing required packages
from flask import Flask

# create application
app = Flask(__name__)

# import routes
from application import routes
