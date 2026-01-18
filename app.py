from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/helloWorld')
def hello():
    return "Hello world!"

#dynamic route examples
@app.route('/greet/<name>')
def great(name):
    return f"Hello, {name}!"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)