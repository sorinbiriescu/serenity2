import os
# A very simple Flask Hello World app for you to get started with...

from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

#Application configuration
app = Flask(__name__)
app.config["DEBUG"] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
WTF_CSRF_ENABLED = True
app.config['SECRET_KEY'] = 'pmooihjq9898+sdncoevhl65oksdh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db/serenity2.db')
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)

JOBS_PER_PAGE = 15

import models
import views