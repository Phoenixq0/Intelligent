from flask import Flask
import config
from exts import db
from bluepirints.qa import ath as qa_blueprint
from flask_migrate import Migrate
from flask_cors import CORS
from models import Department, Doctor, Article


app = Flask(__name__)
#配置文件
CORS(app)
app.config.from_object(config)


db.init_app(app)
with app.app_context():
    db.create_all()
    

migrate=Migrate(app, db)

#蓝图

app.register_blueprint(qa_blueprint)

app.config['JSON_AS_ASCII'] = False  # 设置为False以支持中文字符

if __name__ == '__main__':
    app.run(debug=True)
    app.config['JSON_AS_ASCII'] = False 