from flask import Flask, request, make_response
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

#adding second parameter after return to specify status code
@app.route('/hello')
def hello():
    response = make_response("Hello, World!\n")
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response


#methods param indicates which HTTP methods are allowed
@app.route('/helloWorld', methods=['GET', 'POST'])
def hello_world():
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