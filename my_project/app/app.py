from flask import Flask
import redis
import psycopg2
from elasticsearch import Elasticsearch

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379)

pg_conn = psycopg2.connect(
    host="db",
    database="your_database",
    user="your_username",
    password="your_password"
)

es = Elasticsearch(['http://elasticsearch:9200'])

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
