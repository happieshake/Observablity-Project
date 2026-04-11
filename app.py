from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# 1. Create a Counter metric to track requests
# Counters only ever go up (perfect for tracking totals)
REQUEST_VISITS = Counter('my_app_visits_total', 'Total number of visits to the home page')

@app.route('/')
def home():
    # 2. Every time someone visits this route, increment the counter by 1
    REQUEST_VISITS.inc()
    return "Hello! I am a Python app, and I am being monitored."

@app.route('/metrics')
def metrics():
    # 3. Expose the metrics on a /metrics endpoint so Prometheus can scrape them
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)