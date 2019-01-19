from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
    
def hola():
    return 'Hola'
    
@app.route('/segunda')

def segunda():
    return 'Segunda'

@app.route('/tercera')

def tercera():
    return 'This is la tercera'

@app.route('/segunda/<string:name>/')

def nombre(name):
    return name

@app.route('/hola/<string:name>/')

def hola1(name):
    return render_template('test.html',name=name)



app.run()