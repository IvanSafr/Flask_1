from flask import Flask, render_template, url_for

app = Flask(__name__)

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