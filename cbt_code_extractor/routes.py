from flask import render_template, request, flash, jsonify
from cbt_code_extractor import app, cnx


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index', methods=['POST'])
def index():
    if request.method == 'POST':
        codes = request.form['cbt_code']
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM cbt_code where id IN (%s)" % codes)
        result = cursor.fetchall()
    return render_template('download.html', result=result)


@app.route('/download', methods=['GET', 'POST'])
def download():
    cnx.cursor().close()
    cnx.close()
    return render_template('download.html')
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
