#-*- encoding=UTF-8 -*-
#模块导出文件
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)  #建立 app
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf') #
app.secret_key='nowcoder'
db=SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view='/regloginpage/'

from nowstagram import  views,models