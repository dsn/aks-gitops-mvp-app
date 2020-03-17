from flask import Flask
from flask import abort
import lorem
import logging
import time


app = Flask(__name__)

# Disable accessive logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/error/500')
def error500():
	abort(500, description="internal server error")

@app.route('/')
def hello_world():
	# Add latency
	time.sleep(2)
    return 'Flask: Hello World from Canary Deployment v19'


@app.route('/version')
def version():
    return 'V19'


@app.route('/log')
def log():
    paragraph = lorem.paragraph()
    print(paragraph, flush = True)
    return paragraph

@app.route('/api')
def rest_hello_world():
    return '{"id":1,"message":"Flask: Hello World from Canary Deployment"}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9898)