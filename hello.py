from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    #age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, Name: {self.name}>'


db.create_all()


@app.route('/')
def index():
    name = Person.query.first().name
    return '<h1>Hello '+name+'!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
