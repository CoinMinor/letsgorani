from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 점수 저장용
scores = {
    "1": 0,  # Red Squad
    "2": 0   # Blue Squad
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.get_json()
    team = data.get("team")
    delta = int(data.get("score", 0))

    if team in scores:
        scores[team] += delta
        return jsonify({"status": "success", "updated_score": scores[team]}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid team ID"}), 400

@app.route('/reset_scores', methods=['POST'])
def reset_scores():
    scores["1"] = 0
    scores["2"] = 0
    return jsonify({"status": "success"}), 200

@app.route('/get_scores', methods=['GET'])
def get_scores():
    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True)
