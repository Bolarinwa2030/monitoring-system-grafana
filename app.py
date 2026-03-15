from flask import Flask, Response  # Added Response, removed trailing comma
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus Counter
REQUEST_COUNT = Counter(
    'app_request_count',
    'Total number of requests of the web app'
)

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Project Running"

@app.route('/metrics')
def metrics():
    # Response is now imported from flask
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
