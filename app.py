from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')

@app.route("/services")
def services():
    return render_template('services.html')

if __name__ == "__main__":
    app.run(debug=True)