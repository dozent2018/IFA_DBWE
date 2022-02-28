# kap-2/app/routes.py
from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"