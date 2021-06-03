from flask import Flask, render_template
import yfinance as yf
import pandas as pd
from datetime import date
from matplotlib import pyplot as plt
import seaborn as sns

avg = pd.read_csv("snittt.csv", encoding="ISO-8859-1")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("homepage.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/portfolio')
def portofølja():
    return render_template("portfolio.html")

@app.route('/snitt')
def snitt():
    return render_template("snitt.html", avg=avg)

@app.route('/max')
def max():
    return render_template("max.html")