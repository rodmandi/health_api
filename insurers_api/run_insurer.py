from flask import Flask, jsonify, request

app_insurer = Flask(__name__)


@app_insurer.route('/api1', methods=['POST'])
def create_insurer_api1():
    task = {
        'deductible': 1000,
        'stop_loss': 10000,
        'oop_max': 5000
    }
    return jsonify(task), 200

@app_insurer.route('/api2', methods=['POST'])
def create_insurer_api2():
    task = {
        'deductible': 1200,
        'stop_loss': 13000,
        'oop_max': 6000
    }
    return jsonify(task), 200

@app_insurer.route('/api3', methods=['POST'])
def create_insurer_api3():
    task = {
        'deductible': 1000,
        'stop_loss': 10000,
        'oop_max': 6000
    }
    return jsonify(task), 200


if __name__ == '__main__':
    app_insurer.run(host="0.0.0.0", port=6000, debug=True)