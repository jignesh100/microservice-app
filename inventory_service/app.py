from flask import Flask, jsonify
app = Flask(__name__)
INVENTORY = [{"product_id": 1, "stock": 50}, {"product_id": 2, "stock": 100}]

@app.route("/inventory")
def get_inventory():
    return jsonify(INVENTORY)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
