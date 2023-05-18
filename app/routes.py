from app import app
from flask import render_template
from app.forms import CreateReviewForm

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/review')
@app.route('/review/')  
def review():
    return render_template('review.html', title='Review')

@app.route('/review/create')
def create():
    form = CreateReviewForm()
    return render_template('create.html', title='Create Review', form=form)

@app.route('/help-center')
def help():
    return render_template('help.html', title='Help Center')

@app.route('/confirm')
def confirm():
    return render_template('confirm.html', title='Confirm')