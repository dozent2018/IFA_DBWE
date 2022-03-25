# kap-3.2.2 /app/routes.py mit weiterem Template
from flask import render_template
from app import app

# Test Templates 1
@app.route('/')
@app.route('/index')
def index():
    user = 'Jochen'
    # return render_template('hello_user.html', title='Home', name=user)
    # return render_template('hello_if.html', name=user)
    return render_template('hello_if.html', title='Home')

# Test Templates 2
@app.route('/looptest')
def looptest():
    user = 'Jochen'
    zeilen = ['Beliebig viele Zeilen in einer Liste',
    'Diese Zeile ist die erste',
    'Und das ist die zweite','und noch die dritte']
    return render_template('hello_for.html', name=user,
                            title='Schleifen', lines=zeilen)

# Test Templates 3 macros
@app.route('/macrotest')
def macrotest():
    user = 'Jochen'
    zeilen = ['Beliebig viele Zeilen in einer Liste',
    'Diese Zeile ist die erste',
    'Und das ist die zweite','und noch die dritte']
    return render_template('hello_macro.html', name=user,
                            title='Makros', lines=zeilen)

# Test Templates 4
@app.route('/inheritance')
def inheritance():
    return render_template('hello_derived.html')