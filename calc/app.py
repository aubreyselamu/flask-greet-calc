from flask import Flask, request
from operations import add, sub, div, mult


app = Flask(__name__)


@app.route('/add')
def do_add():
    '''Add a and b parameters '''
    
    a = int(request.args.get('a')) #what is the purpose of get?
    b = int(request.args.get('b'))
    result = add(a,b)

    return str(result)


@app.route('/sub')
def do_subtract():
    '''Subtract a and b parameters'''
    
    a = int(request.args.get('a')) 
    b = int(request.args.get('b'))
    result = sub(a,b)

    return str(result)

@app.route('/div')
def do_division():
    '''Divide a and b parameters'''
    
    a = int(request.args.get('a')) 
    b = int(request.args.get('b'))
    result = div(a,b)

    return str(result)

@app.route('/mult')
def do_multiplication():
    '''Multiply a and b parameters'''
    
    a = int(request.args.get('a')) 
    b = int(request.args.get('b'))
    result = mult(a,b)

    return str(result)