from flask import Flask, request, jsonify
import leveldb
import json

# Open (or create) the LevelDB database in ./state
try:
    db = leveldb.LevelDB("./state", create_if_missing=True)
except Exception as e:
    print("Error opening LevelDB database:", e)
    raise

app = Flask(__name__)

@app.route("/query/<tweet_id>", methods=["GET"])
def query(tweet_id):
    """Return the stored transaction for a given tweet_id."""
    try:
        raw_value = db.Get(tweet_id.encode())
        data = json.loads(raw_value.decode())
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": f"Not found or error: {str(e)}"}), 404

@app.route("/submit", methods=["POST"])
def submit():
    """Store a new transaction. Required fields: tweet_id, zone_id, hazard, status, timestamp."""
    try:
        tx = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON payload"}), 400

    required_fields = {"tweet_id", "zone_id", "hazard", "status", "timestamp"}
    if not required_fields.issubset(tx):
        return jsonify({"error": f"Missing required fields: {required_fields}"}), 400

    try:
        db.Put(tx["tweet_id"].encode(), json.dumps(tx).encode())
        return jsonify({"result": "success"}), 200
    except Exception as e:
        return jsonify({"error": f"Error writing to database: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
