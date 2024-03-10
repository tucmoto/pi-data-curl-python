from trackcurl import db

class Repetition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)

    def __init__(self, date, reps, weight):
        self.date = date
        self.reps = reps
        self.weight = weight
