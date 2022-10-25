from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)