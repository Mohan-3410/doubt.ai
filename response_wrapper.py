from flask import jsonify

def success(status_code, result):
    return jsonify({
        'status': 'ok',
        'statusCode': status_code,
        'result': result
    }), status_code

def error(status_code, message):
    return jsonify({
        'status': 'error',
        'statusCode': status_code,
        'message': message
    }), status_code
