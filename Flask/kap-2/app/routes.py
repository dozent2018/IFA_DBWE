# kap-2/app/routes.py
from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"

from flask import request
@app.route('/useragent')
def uagent():
  user_agent = request.headers.get('User-Agent')
  return '<p> Ihr Browser: {}</p>'.format(user_agent)
