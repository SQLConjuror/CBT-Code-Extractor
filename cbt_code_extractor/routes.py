from flask import render_template, request, flash, jsonify
from cbt_code_extractor import app, cnx
import json


@app.route('/')
def home():
    cursor = cnx.cursor()
    query = "SELECT * FROM testdb WHERE id=1"
    cursor.execute(query)
    for (item) in cursor:
        print("id: '" + str(item[0]) + "', code: '" + str(item[1]) + "'")
    cursor.close()
    cnx.close()
    return jsonify(item)


@app.route('/index')
def index():
    if request.method == 'POST':
        return request.form['cbt_code']
        # flash('Sample flash message')
    return render_template('index.html')


@app.route('/download', methods=['GET', 'POST'])
def download():
    return render_template('download.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
