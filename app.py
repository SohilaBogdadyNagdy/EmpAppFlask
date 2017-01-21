from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL ()
print (mysql)
app = Flask(__name__)
app.config.from_object('config')
#print (app.config)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1qaz5tgb'
app.config['MYSQL_DATABASE_DB'] = 'FLASKDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)






import views