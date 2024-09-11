from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def get_whitepaper():
    return jsonify("Hello i am backend")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
