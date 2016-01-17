from catalog import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(1000), nullable=False)
    picture = db.Column(db.String(1000))
    catagory_items = db.relationship(
        'CatagoryItem',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, name, email, picture, items=[]):
        self.name = name
        self.email = email
        self.picture = picture
        self.catagory_items = items

    def __repr__(self):
        return '<User {0}>'.format(self.email)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.email,
            'picture': self.picture
        }


class Catagory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    catagory_items = db.relationship(
        'CatagoryItem',
        backref='catagory',
        lazy='dynamic'
    )

    def __init__(self, name, items=[]):
        self.name = name
        self.catagory_items = items

    def __repr__(self):
        return '<Catagory {0}>'.format(self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'items': [ci.serialize for ci in self.catagory_items]
        }


class CatagoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    author = db.Column(db.String(1000))
    description = db.Column(db.Text)
    picture = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    catagory_id = db.Column(db.Integer, db.ForeignKey('catagory.id'))

    def __init__(self, name, author, description, picture, catagory_id,
                 user_id=None):
        self.name = name
        self.author = author
        self.description = description
        self.picture = picture
        self.user_id = user_id
        self.catagory_id = catagory_id

    def __repr__(self):
        return '<CatagoryItem {0}>'.format(self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description,
            'picture': self.picture
        }
