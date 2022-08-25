from flask import render_template, request, flash, jsonify, send_file
from cbt_code_extractor import app, cnx
import pandas as pd


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index', methods=['POST'])
def index():
    if request.method == 'POST':
        Code = str(request.form['cbt_code']).strip()
        if Code:
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM cbtcode where Code IN ('%s')" % Code)
            # cursor.execute("SELECT * FROM cbtcode WHERE IntlOpenId <> 'NULL'")
            result = cursor.fetchall()
            if result:
                return render_template('index.html', result=result)
            else:
                flash("CBT code not found in Database! Please enter a valid CBT code", category="error")
                return render_template('index.html')
        else:
            error = 'Please enter a valid CBT code'
            return render_template('index.html', error=error)
    return render_template('index.html')


@app.route('/download', methods=['GET','POST'])

def download():
    if request.method == 'POST':
        if request.form['download'] == 'Download Used CBT Code in csv Format':
            cursor1 = cnx.cursor()
            cursor1.execute("SELECT * FROM cbtcode WHERE IntlOpenId <> 'NULL'") 
            result1 = cursor1.fetchall()
            if result1:
                headers = ['Code', 'IntlOpenId']
                df = pd.DataFrame(data=result1, columns=headers)
                df.to_csv(r'/root/flask-app/CBT-Code-Extractor/output/exported_data.csv',
                            index=False)
                path = "/root/flask-app/CBT-Code-Extractor/output/exported_data.csv"
                return send_file(path, as_attachment=True)
    return render_template('download.html')

