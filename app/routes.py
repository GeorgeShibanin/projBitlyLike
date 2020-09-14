from flask import render_template, request, redirect
from app.forms import emptyBlank
from app import app
from app.functions import short_save, return_url


@app.route('/', methods=['GET', 'POST'])
def change_url():
    form = emptyBlank()
    if form.validate_on_submit():
        return short_save(request.form['url'], request.form['custom'])
    return render_template('main.html', title='Change URL', form=form)


@app.route('/<string:url>', methods=['GET'])
def forward(url):
    return redirect(return_url(url))
