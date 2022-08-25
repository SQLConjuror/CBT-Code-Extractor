from flask import Flask
from flask_bootstrap import Bootstrap
import mysql.connector


app = Flask(__name__)
app.secret_key = "super secret key"
Bootstrap(app)

_config = {
    'user': 'smartlink@test-smartlink-data-extraction',
    'password': 'Supp0rt#12',
    'host': 'test-smartlink-data-extraction.mysql.database.azure.com',
    'database': 'nkmanager',
    'raise_on_warnings': True,
    }
cnx = mysql.connector.connect(**_config)


from cbt_code_extractor import routes
