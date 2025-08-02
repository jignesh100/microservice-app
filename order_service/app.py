from flask import Flask, jsonify
app = Flask(__name__)
ORDERS = [{"id": 1, "user_id": 1, "product_id": 2}]

@app.route("/orders")
def get_orders():
    return jsonify(ORDERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
