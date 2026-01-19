from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    my_list = [1, 2, 3, 4, 5]
    return render_template('index.html', my_list=my_list)

@app.route('/other')
def other():
    some_text = "This is some other text."
    return render_template('other.html', some_text=some_text)

#filters
@app.template_filter('reverse')
def reverse_filter(str):
    return str[::-1]

@app.template_filter('repeat')
def repeat_filter(str, times=2):
    return str * times
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)