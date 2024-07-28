from flask import Flask, request, jsonify
from flask_cors import CORS

appa = Flask(__name__)
CORS(appa)  # Enable CORS for all routes

@appa.route('/api/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get('name', '')
    return jsonify({"greeting": f"Hello, {name}!"})

if __name__ == '__main__':
    appa.run(debug=True)