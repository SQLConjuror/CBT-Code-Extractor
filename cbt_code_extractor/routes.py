from flask import render_template, request, flash, jsonify
from cbt_code_extractor import app, cnx
import pandas as pd


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index', methods=['POST'])
def index():
    if request.method == 'POST':
        codes = request.form['cbt_code']
        if codes:
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM cbt_code where id IN (%s)" % codes)
            result = cursor.fetchall()
            if result:
                headers = ['Code', 'IntlOpenId']
                df = pd.DataFrame(data=result, columns=headers)
                df.to_csv(r'/home/zubair/Desktop/dashboard/Upwork Ongoing/CBT-Code-Extractor/exported_data.csv',
                          index=False)
            else:
                flash("CBT codes not found in Database!", category='danger')
                return render_template('index.html')
        else:
            error = 'Please Enter Valid CBT Codes!'
            return render_template('index.html', error=error)
        return render_template('download.html', result=result)


@app.route('/download')
def download():
    return render_template('thankyou.html')
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)
