from app.models import User
from app import app, db, bcrypt
from flask import render_template, redirect, url_for, request, send_file
from app.forms import LoginForm, RegForm
import logging, os

posts = [
    {
        'author': 'Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/", methods = ['GET', 'POST'])
@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template("login.html", form = form)

@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    form = RegForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, password = hashed_pw, standard = form.standard.data, section = form.section.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    app.logger.debug(form.errors)
    return render_template("signup.html", form = form)

@app.route("/home", methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route("/write", methods =  ['GET', 'POST'])
def write():
    return render_template("writehome.html", posts=posts)

@app.route("/notes", methods = ['GET', 'POST'])
def notes():
    class8_list = os.listdir(app.config["CLASS8_NOTES"])
    class9_list = os.listdir(app.config["CLASS9_NOTES"])
    class10_list = os.listdir(app.config["CLASS10_NOTES"])
    class11_list = os.listdir(app.config["CLASS11_NOTES"])
    class12_list = os.listdir(app.config["CLASS12_NOTES"])

    if request.method == 'POST':
        file = request.files["file"]
        grade = request.form["class"]
        if grade=="8th":
            file.save(os.path.join(app.config["CLASS8_NOTES"], file.filename))
        if grade=="9th":
            file.save(os.path.join(app.config["CLASS9_NOTES"], file.filename))
        if grade=="10th":
            file.save(os.path.join(app.config["CLASS10_NOTES"], file.filename))
        if grade=="11th":
            file.save(os.path.join(app.config["CLASS11_NOTES"], file.filename))
        if grade=="12th":
            file.save(os.path.join(app.config["CLASS12_NOTES"], file.filename))
    
    return render_template("notes-home.html",
                            class8_list=class8_list,
                            class9_list=class9_list,
                            class10_list=class10_list,
                            class11_list=class11_list,
                            class12_list=class12_list)

@app.route('/notes/export/<grade>/<file>/')
def export_notes(grade, file):
    path = os.path.join(app.config[f"CLASS{grade}_NOTES"][4:], file)
    return send_file(path)
