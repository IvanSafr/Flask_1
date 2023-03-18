from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class DatB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=dt.utcnow)

    def __repair__(self):
        return '<DatB %r' %self.id

@app.route('/library')
def posts_page():
    posts = DatB.query.order_by(DatB.date).all()

    return render_template("posts.html", posts=posts)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        art = DatB(title=title, intro=intro, text=text)
        try:
            db.session.add(art)
            db.session.commit()
            return redirect('/')
        except:
            return "Еклмн, ошибка"


    else:
        return render_template("create.html")

@app.route('/us')
def us():
    return render_template("about.html")

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User: " + name +" " + str(id)


if __name__ == '__main__':
    app.run(debug=True)