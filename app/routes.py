from flask import render_template, request, redirect
from app.forms import emptyBlank
from app import app, db
from app.models import Href

import requests
import random
import string

my = "http://georgeshibanin.pythonanywhere.com/"


@app.route('/', methods=['GET', 'POST'])
def changeurl():
    form = emptyBlank()
    if form.validate_on_submit():
        url = request.form['url']
        cust = request.form['custom']
        if requests.get(url).status_code != 200:
            return "your link is not valid"
        a = Href.query.filter_by(url=url).first()

        if not a:
            if cust != '':
                newurl = cust
            else:
                newurl = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for x in range(8))
            href = Href(url, newurl)
            db.session.add(href)
            db.session.commit()
            return my + newurl
        else:
            return my + db.session.query(Href.new_url).filter(Href.url == url).scalar()
    return render_template('main.html', title='Change URL', form=form)


@app.route('/<string:url>', methods=['GET'])
def redir(url):
    if not Href.query.filter_by(new_url=url).first():
        return "No such url"
    res = db.session.query(Href.url).filter(Href.new_url == url).scalar()
    return redirect(res)
