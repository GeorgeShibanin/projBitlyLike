from app import db


class Href(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), unique=True)
    new_url = db.Column(db.String(16), unique=True)

    def __init__(self, url, new_url):
        self.url = url
        self.new_url = new_url

