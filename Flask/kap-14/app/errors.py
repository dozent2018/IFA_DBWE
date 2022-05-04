from flask import render_template, request, jsonify
from app import app, db
from werkzeug.http import HTTP_STATUS_CODES

@app.errorhandler(404)
def not_found_error(error):
    if request.accept_mimetypes.accept_json and \
    not request.accept_mimetypes.accept_html:
        response = jsonify( {'error': 'Not Found'} )
        response.status_code = 404
        return response
    else:
        return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    if request.accept_mimetypes.accept_json and \
    not request.accept_mimetypes.accept_html:
        response = jsonify( {'error': 'Internal Server Error' } )
        response.status_code = 500
        return response
    return render_template('500.html'), 500

def error_response(status_code, message=None):
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response

def bad_request(message):
    return error_response(400, message)
