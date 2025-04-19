import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import openpyxl  # 如果没有报错，说明安装成功
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pickle
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 50)

# 读取数据
df = pd.read_json("../data/patient_records.json")

print(df.head())

# 自变量和因变量
X = df[["age", "chief_complaint", "present_illness_history", "physical_exam"]]
Y = df["primary_diagnosis_name"]

# 将数据集分为训练和测试
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

# 分离数值型和非数值型特征
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = X.select_dtypes(include=['object']).columns

# 构建预处理管道
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),  # 对数值型特征进行标准化
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)  # 对非数值型特征进行独热编码
    ])

# 构建管道
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())  # 使用随机森林分类器
])

# 尝试训练模型并保存
try:
    pipeline.fit(X_train, Y_train)
    # 确保保存路径存在
    os.makedirs(os.path.dirname("model.pkl"), exist_ok=True)
    pickle.dump(pipeline, open("model.pkl", "wb"))
    print("Model saved successfully.")
except Exception as e:
    print(f"An error occurred: {e}")