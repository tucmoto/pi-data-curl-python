
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repetitions.db'
db = SQLAlchemy(app)
CORS(app)

from models import Repetition
db.create_all()


class Repetition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(50))
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)

    def __init__(self, date, reps, weight):
        self.date = date
        self.reps = reps
        self.weight = weight

@app.route('/repetitions', methods=['GET'])
def get_repetitions():
    repetitions = Repetition.query.all()
    output = []
    for repetition in repetitions:
        repetition_data = {'id': repetition.id, 'date': repetition.date, 'reps': repetition.reps, 'weight': repetition.weight}
        output.append(repetition_data)
    return jsonify({'repetitions': output})

@app.route('/repetitions', methods=['POST'])
def add_repetition():
    data = request.get_json()
    new_repetition = Repetition(date=data['date'], reps=data['reps'], weight=data['weight'])
    db.session.add(new_repetition)
    db.session.commit()
    return jsonify({'message': 'Repetition added'})

if __name__ == '__main__':
    app.run(debug=True)
