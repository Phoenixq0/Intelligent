from exts import db
from datetime import datetime
import app

class Doctor(db.Model):
    """医生模型类"""
    __tablename__ = 'doctor'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=True)
    title=db.Column(db.String(50), nullable=False)  # 职称
    department=db.Column(db.String(50), nullable=False)  # 科室
    hospital=db.Column(db.String(50))  # 医院
    description=db.Column(db.Text, nullable=True)  # 简介
    treatmentkeywords=db.Column(db.JSON)  # 擅长治疗的关键词
    available=db.Column(db.Boolean, default=True)  # 是否可预约
    created_at = db.Column(db.DateTime, default=datetime.now)  # 注册时间

class Department(db.Model):
    """科室模型类"""
    __tablename__ = 'department'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=False, nullable=False)  # 科室名称
    description = db.Column(db.Text)  # 科室描述
    keywords = db.Column(db.JSON)  # 科室关键词
    created_at = db.Column(db.DateTime, default=datetime.now)  # 创建时间

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'keywords': self.keywords if self.keywords else [],
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            # 可以根据需要添加其他字段
        }
  
class Article(db.Model):
    """文章模型类"""
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keycontent = db.Column(db.JSON)  # 文章关键词
    title = db.Column(db.String(100), nullable=False)  # 文章标题
    content = db.Column(db.Text)  # 文章内容
    author = db.Column(db.String(50) , nullable=True)  # 作者
    created_at = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 更新时间




