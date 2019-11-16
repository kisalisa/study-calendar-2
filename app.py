import pyrebase
from flask import Flask, render_template, request, redirect, session, url_for
import os
import keys

app = Flask(__name__)

config = {
    "apiKey": keys.APIKEY,
    "authDomain": keys.AUTHDOMAIN,
    "databaseURL": keys.DATABASEURL,
    "projectId": keys.PROJECTID,
    "storageBucket": keys.STORAGEBUCKET,
    "messagingSenderId": keys.MESSAGINGSENDERID,
    "appId": keys.APPID
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

@app.route("/", methods=['GET', 'POST'])

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     if(request.method == 'POST'):
#         email = request.form['email']
#         username = request.form['username']
#         password = request.form['password']
#         try:
#             auth.sign_in_with_email_and_password(email, password)
#             return render_template('user.html')
#         except:
#             auth.create_user_with_email_and_password(email, password)
#             db.child("users").push({"name" : username})
#             return render_template("validprofile.html")
#     return render_template("login.html")
# @app.route("/validprofile")
# def validprof():
#     return render_template('validprofile.html')

@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/class_form.html")
def class_form():
    return render_template('class_form.html')

@app.route("/create_calendar.html")
def create_calendar():
    return render_template('create_calendar.html')

@app.route("/schedule_class.html")
def schedule_class():
    return render_template('schedule_class.html')

@app.route("/schedule_midterm.html")
def schedule_midterm():
    return render_template('schedule_midterm.html')

@app.route("/study_hours.html")
def study_hours():
    return render_template('study_hours.html')

@app.route("/test_form.html")
def test_form():
    return render_template('test_form.html')


"""
# entry from user.html
@app.route("/create_cookbook.html", methods=['GET', 'POST'])
def create_cookbook():
    if(request.method == 'POST'):
        booktitle = request.form['CookbookTitle']
        db.push({'CookbookTitle' : booktitle})
        return redirect(url_for('create_recipe', currentbook = booktitle))
    return render_template('create_cookbook.html')

# entry from cookbook.html
@app.route("/create_recipe.html", methods=['GET', 'POST'])
def create_recipe():
    if(request.method == 'POST'):
        name = request.form['RecipeName']
        #db.child(currentbook).push({"name" : name})
        info = {
            "Introduction" : request.form['Introduction'],
            "PrepTime" : request.form['PrepTime'],
            "CookTime" : request.form['CookTime'],
            "TotalTime" : request.form['TotalTime'],
            "Ingredients" : request.form['Ingredients'],
            "Servings" : request.form['Servings'],
            "Instructions" : request.form['Instructions']
        }
        db.child(request.args['currentbook']).push({name : info})
        return redirect(url_for('recipe', name = name, currentbook = request.args['currentbook']))
    return render_template('create_recipe.html', currentbook = request.args['currentbook'])

@app.route("/cookbook.html")
def cookbook():
    return render_template("cookbook.html", currentbook = request.args['currentbook'])

@app.route("/recipe.html")
def recipe():
    ref = db.child(request.args['currentbook']).child(request.args['name'])
    intro = ref.child("Introduction").get()
    prepT = ref.child("PrepTime").get()
    cookT = ref.child("CookTime").get()
    totalT = ref.child("TotalTime").get()
    ingre = ref.child("Ingredients").get()
    servings = ref.child("Servings").get()
    instruc = ref.child("Instructions").get()
    return render_template("recipe.html", name = request.args['name'], ref = ref, intro = intro, prepT = prepT, cookT = cookT, totalT= totalT, ingre = ingre, servings = servings, instruc = instruc)
"""

if __name__ == '__main__':
    app.run(debug = True)