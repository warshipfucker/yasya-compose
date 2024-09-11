import logging
from pymongo import MongoClient
from flask import Flask

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongodb:27017/')
db = client.logs
log_collection = db.backend_logs

# Log handler that sends logs to MongoDB
class MongoHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        log_collection.insert_one({"log": log_entry})

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
mongo_handler = MongoHandler()
logger.addHandler(mongo_handler)

@app.route('/')
def home():
    logger.info('Home page accessed')
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
