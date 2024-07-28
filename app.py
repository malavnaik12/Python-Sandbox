from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get('name', '')
    return jsonify({"greeting": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True)