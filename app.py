from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Backend is working!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # 模拟预测逻辑，可以之后接入真实模型
    feature1 = data.get('feature1', 0)
    feature2 = data.get('feature2', 0)

    result = {
        "prediction": "Gold price might go UP ⬆️" if feature1 + feature2 > 200 else "Gold price might go DOWN ⬇️",
        "input": data
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
