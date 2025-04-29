from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    # При локальном запуске (без Docker)
    app.run(host="0.0.0.0", port=8000, debug=True)
