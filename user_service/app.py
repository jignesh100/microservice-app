from flask import Flask, jsonify
app = Flask(__name__)
USERS = [{"id": 1, "name": "Jignesh"}, {"id": 2, "name": "Verulakar"}]

@app.route("/users")
def get_users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
