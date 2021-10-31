from flask import Flask, app, render_template, request
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('interface.html')

@app.route('/', methods = ['POST'])
def result():
    plainText = request.form.get("var_1", type=str)