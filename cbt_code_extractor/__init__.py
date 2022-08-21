from flask import Flask
from flask_bootstrap import Bootstrap
import mysql.connector


app = Flask(__name__)
Bootstrap(app)

# cnx = mysql.connector.connect(user='root', password='root',
#                               host='127.0.0.1', database='testdb')
_config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'testdb',
    'raise_on_warnings': True,
    }
cnx = mysql.connector.connect(**_config)


from cbt_code_extractor import routes
