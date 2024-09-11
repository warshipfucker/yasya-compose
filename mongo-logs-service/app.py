from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Подключение к MongoDB
client = MongoClient('mongodb://mongodb:27017/')
db = client.logs
log_collection = db.logs

@app.route('/log', methods=['POST'])
def collect_log():
    log_data = request.json
    if not log_data or 'message' not in log_data:
        return jsonify({"error": "Invalid log data"}), 400

    log_collection.insert_one({"message": log_data['message'], "level": log_data.get('level', 'INFO')})
    return jsonify({"status": "Log stored successfully"}), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = list(log_collection.find({}, {'_id': 0}))
    return jsonify(logs), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
