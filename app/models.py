from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable = False, unique = True)
    password = db.Column(db.String(50), nullable = False)
    standard = db.Column(db.String, nullable = False)
    section = db.Column(db.String(2), nullable = False)
    profile_image = db.Column(db.String(50), default = 'default.jpg')
    posts = db.relationship('WritePost', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.standard}', '{self.section}')"

class WritePost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"WritePost('{self.title}', '{self.date_posted}')"