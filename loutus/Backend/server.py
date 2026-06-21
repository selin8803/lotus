from flask import Flask, request, jsonify
from flask_cors import CORS
from Entropy import load_data, build_tree, predict

app = Flask(__name__)
CORS(app)

data = load_data()
tree = build_tree(data)
@app.route("/")
def home():
    return "Server is working"
@app.route("/api/predict", methods=["POST"])
def predict_api():

    sample = request.json

   
    if (
    sample["sleep"] < 1 or sample["sleep"] > 12 or
    sample["Meetings"] < 0 or sample["Meetings"] > 10 or
    sample["Stress"] < 1 or sample["Stress"] > 10 or
    sample["Weekends"] not in ["Yes", "No"]
     ):
     return jsonify({"error": "Invalid input"}), 400
    result = predict(tree, sample)
    print(result)

    return jsonify({
        "prediction": result
    })
@app.route("/api/train", methods=["POST"])
def train():

    global tree

    data = load_data()
    tree = build_tree(data)

    return jsonify({
        "message": "Model trained successfully"
    })
@app.route("/api/tree", methods=["GET"])
def get_tree():

    return jsonify(tree)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)