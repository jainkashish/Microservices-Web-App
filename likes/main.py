from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

from producer import publish
from producer import publish2

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/likes'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

@app.route('/')
def index():
    return 'hello'


@app.route('/api/user/product/like', methods=['GET'])
def like():
    json_user = requests.get(
        'http://docker.for.win.localhost:8002/api/user').json()
    json_product = requests.get(
        'http://docker.for.win.localhost:8003/api/product').json()
    try:
        productUser = Likes(
            user_id=json_user['id'], product_id=json_product['id'])
        db.session.add(productUser)
        db.session.commit()
        publish('product_liked', json_product['id'])
        publish2('user_liked', json_user['id'])
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success',
        'user_id': json_user['id'],
        'product_id': json_product['id']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
