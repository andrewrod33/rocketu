import logging
from bottle import request, route, run

@route('/log/<name>')
def index (name='Anonymous'):
    level = int(request.query.levelno)
    print name.upper(),
    print logging.getLevelName(level),
    print request.query.msg
    return 'OK'

run(host='localhost', port=8080)
