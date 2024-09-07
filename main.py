from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLite'ı bağlama
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)

class Forum(db):
    id = db.Column(db.Integer, primary_key = True, autoincrement = False)

    name = db.Column(db.String(85), nullable = False)
    title = db.Column(db.String(25), nullable = False)
    text = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f'<User {self.id}>'
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    # result.html'e Forum sınıfındaki verileri db'den aktarma
    blogs = Forum.query.order_by(Forum.id).all()

    return render_template('result.html', blogs=blogs)