from flask import Flask, render_template, url_for, request, redirect, flash, session
from . import app
  

import smtplib
import os



@app.route("/")
def home():
    return render_template('index.html')






if __name__ == "__main__":
    app.run(debug=True)
