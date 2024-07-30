from flask import Flask, render_template, request, session, redirect, send_from_directory

app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/")
def get_sitemap():
    return render_template('index.html', titleText = 'Hello World!')