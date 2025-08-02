from flask import Flask, jsonify
app = Flask(__name__)
PRODUCTS = [{"id": 1, "name": "Book"}, {"id": 2, "name": "Pen"}]

@app.route("/products")
def get_products():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
