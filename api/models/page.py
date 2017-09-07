from app import db

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255))
    title = db.Column(db.String(64))
    content = db.Column(db.String(9999))

    def __repr__(self):
        return '<Page %r>' % (self.title)
