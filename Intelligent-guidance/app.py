import time

import numpy as np
from flask import Flask, request, jsonify, render_template
from models.deepseek import DeepSeekAPI
import pickle

# 创建flask应用
app = Flask(__name__)

# 加载模型

model = pickle.load(open("models/model.pkl", "rb"))
deepseek_api = DeepSeekAPI()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 获取表单数据
        symptom_text = request.form.get('symptom', '').strip()

        if not symptom_text:
            return render_template("index.html", error="请输入症状描述")

        # try:
        #     # BERT模型预测
        #     # start_time = time.time()
        #     # diagnosis = bert_model.predict(symptom_text)
        #     # bert_time = time.time() - start_timex

        # DeepSeek建议
        start_time = time.time()
        advice = deepseek_api.get_advice(symptom_text)
        deepseek_time = time.time() - start_time

        return render_template('index.html',
                               # diagnosis=diagnosis,
                               advice=advice,
                               # inference_time=f"BERT: {bert_time:.2f}s, DeepSeek: {deepseek_time:.2f}s"
                               )

        # except Exception as e:
        #     print(f"预测错误: {str(e)}")
        #     return render_template('index.html', error="系统处理出现异常，请稍后再试")


# @app.route("/predict", methods=["POST"])
# def predict():
#     float_feature = [float(x) for x in request.form.values()]
#     features = [np.array(float_feature)]
#     prediction = model.predict(features)
#
#     return render_template("index.html", prediction_text="{}".format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
