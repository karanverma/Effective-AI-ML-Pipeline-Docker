
from flask import Flask
import redis
import os

# Initialize Flask app
app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_client = redis.StrictRedis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def index():
    try:
        # Increment the number of visits
        visits = redis_client.incr('counter')
    except redis.exceptions.ConnectionError as e:
        visits = f"Error: {e}"

    return f"Hello! You have visited this page {visits} times."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
