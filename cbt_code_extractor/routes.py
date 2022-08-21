from flask import render_template, request, flash, jsonify
from cbt_code_extractor import app, cnx


@app.route('/')
def home():
    # cursor = cnx.cursor()
    cursor = cnx.cursor(buffered=True)
    query = cursor.execute("select * from testdb;")
    # cursor.close()
    # cnx.close()
    print(query)
    return jsonify(query)


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
