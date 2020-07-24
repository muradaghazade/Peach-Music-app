from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("Peach")
app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite://mydatabase.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column('id', db.Integer, Primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, first_name, last_name, email):
     self.first_name = first_name
     self.email = email
     self.last_name = last_name
     self.password = password

@app.route('/')
def show_all():
    return render_template("index.html", users = User.query.all())


@app.route('/user', methods=['POST', 'GET'])
def create_user():
    if request.method == 'GET':        
        return render_template("new.html")
    else:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        user = User(first_name, last_name, email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('show_all'))


if __name__ == 'Peach':
    db.create_all()
    app.run()