from flask import Flask
from urllib.parse import quote

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)

app.secret_key = "&(^(*&*(&)(*()**^*&%^&TGUYF^%FG&G&GH*IUY(*&*%*%^(*&(*%^&TG"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote("Admin@123")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 6
db = SQLAlchemy(app)
