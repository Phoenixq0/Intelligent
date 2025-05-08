from flask import Blueprint
from flask import request, jsonify
from models import Department, Doctor, Article
from sqlalchemy import or_
import logging
from flask import session

logging.basicConfig(level=logging.DEBUG)
# prediction_cache={}
ath=Blueprint('qa', __name__, url_prefix='/')

#与模型app预测路由合并
# @app.route("/predict", methods=["POST"])
# def predict():
#     float_feature = [float(x) for x in request.form.values()]
#     features = [np.array(float_feature)]
#     prediction = model.predict(features)
#     session['prediction'] = prediction.tolist() #增加会话获取预测
#     return render_template("index.html", prediction_text="{}".format(prediction))

    
@ath.route('/recommend', methods=['GET'])

def recommend():

    result = session.get('prediction')
    if not result:
        return jsonify({'message': '未获得预测结果'}), 404
    
    # 匹配科室
    department = matchDepartment(result)
    logging.debug(f"Matched departments: {department}")
    if not department:
        return jsonify({'message': '没有找到相关科室'}), 404
    
    # 医生推荐（去重）
    re_doctor = []
    seen_doctor_ids = set()
    for doc in department:
        doctors = Doctor.query.filter_by(
            department_id=doc.id,
            available=True
        ).order_by(Doctor.rating.desc()).limit(3).all()
        logging.debug(f"Doctors for department {doc.id}: {doctors}")
        for doctor in doctors:
            if doctor.id not in seen_doctor_ids:
                seen_doctor_ids.add(doctor.id)
                re_doctor.append(doctor)
 
    

    articles = []
    keywords = result
    if keywords:
        conditions = [Article.keycontent.contains(kw) for kw in keywords]
        articles = Article.query.filter(or_(*conditions)) \
            .order_by(Article.created_at.desc()).limit(3).all()
    
    return jsonify({
        'department': [d.to_dict() for d in department],
        'doctors': [d.to_dict() for d in re_doctor],
        'recommended_content': [a.to_dict() for a in articles]
    }), 200

def  matchDepartment(result):  
    if not result:
        return []
    
    # 使用 overlap 匹配至少包含一个关键词
    return Department.query.filter(Department.keywords.overlap(result)) .order_by(Department.id).limit(3).all()

@ath.route('/department', methods=['GET'])
def get_department():
    departments = Department.query.all()
    return jsonify(data=[d.to_dict() for d in departments]), 200