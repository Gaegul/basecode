from flask import Flask, jsonify

from config.config import sqlalchemy_url
from model import db
from model.table import Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/', methods=['GET'])
def index():
	return 'Hello World!'


@app.route('/post/<int:id>', methods=['GET'])
def post(id):
	post = Post.query.get(id)

	return jsonify({
		'content': post.content
	})


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8080)
