from views import db

class Profile(db.Model):

    __tablename__ = "profile"
    profile_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ID_number = db.Column(db.Integer, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    work = db.Column(db.Integer, nullable=False)
    degree = db.Column(db.String, nullable=False)
    
    def __init__(self, name, ID_number, phone_number, work, degree):
        self.name = name
        self.ID_number = ID_number
        self.phone_number = phone_number
        self.work = work
        self.degree = degree
