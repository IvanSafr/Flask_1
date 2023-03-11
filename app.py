from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
db = SQLAlchemy(app)

class DatB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=dt.utsnow)

    def __repair__(self):
        return '<DatB %r' %self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/us')
def us():
    return render_template("about.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User: " + name +" " + str(id)


if __name__ == '__main__':
    app.run(debug=True)