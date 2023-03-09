from flask import Flask, jsonify

from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def index():
    return 'It works'


@app.route('/test_db')
def test_db():
    query = """SELECT 1"""
    result = db.session.execute(query).scalar()
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
