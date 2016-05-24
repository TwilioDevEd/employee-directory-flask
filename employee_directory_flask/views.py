from flask import render_template
from . import app


@app.route('/')
def root():
    return render_template('index.html')
