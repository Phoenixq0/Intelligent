

HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='User'
USERNAME='root'
PASSWORD='0000000'
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI



