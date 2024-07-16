from flask import Flask, jsonify 
import logging
from prometheus_client import Counter, Summary, generate_latest


app = Flask(__name__)


#Logs da Aplicação
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("logger_app")
handler = logging.StreamHandler()
formatter = logging.Formatter('{"time": "%(asctime)s", "level": "%(levelname)s", "message":"%(message)s"}')
handler.setFormatter(formatter)
logger.addHandler(handler)

#Métricas Prometheus
REQUEST_COUNT = Counter('app_requests_total','Numero total de requisições na aplicação')
REQUEST_DURATION = Summary('app_request_duration_seconds', 'Duração dos requests na aplicação')

@app.route('/')
@REQUEST_DURATION.time()
def hello_world():
    msg = 'Hello World Apoena Monitoramento App!'
    logger.info(msg)
    REQUEST_COUNT.inc()
    return jsonify(message=msg)

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}


if  __name__ == "__main__":

    app.run(host='0.0.0.0', port=5000)