from turtle import pd
from flask import Flask, render_template, request, Response

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'dharshaan' and password == 'hi':
            return 'Successfully logged in'
        else:
            return 'Invalid credentials'
        
@app.route('/file-upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode('utf-8')
    elif file.content_type == 'application/pdf':
        content = 'PDF file uploaded successfully.'


@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['file']

    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )

    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)