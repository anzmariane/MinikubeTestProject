from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/hash', methods=['GET'])
def hash_data():
    data_hash = request.json.get('hash')
    if not hash_data:
        return jsonify({"error": "no hash provided"}), 400

    try:
        hashed_value = hashlib.md5(data_hash.encode()).hexdigest()
        return jsonify({"hashed_value": hashed_value}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)