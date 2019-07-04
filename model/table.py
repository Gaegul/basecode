from model import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True),
    content = db.Column(db.String, nullable=False)