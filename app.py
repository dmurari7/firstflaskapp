from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

#methods param indicates which HTTP methods are allowed
@app.route('/helloWorld', methods=['GET', 'POST'])
def hello():
    #create form to get information from user
    if request.method == 'GET':
        return 'You made a GET request' 
    #process the form data
    elif request.method == 'POST':
        return 'You made a POST request' 
    else: 
        return 'Unsupported HTTP method'

#dynamic route examples
@app.route('/greet/<name>')
def great(name):
    return f"Hello, {name}!"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args['name']
        return f'{greeting}, {name}!'
    else:
        return 'Error: not enough parameters'
    

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)