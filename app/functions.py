from flask import request
from app.models import Href
from app import db
import random
import string
import requests


def short_save(url, cust):
    try:
        response = requests.get(url)
    except requests.ConnectionError as exeption:
        return "your link is not valid"
    a = Href.query.filter_by(url=url).first()
    if not a:
        if cust != '':
            newurl = cust
        else:
            newurl = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase) for x in range(8))
        if db.session.query(Href.new_url).filter(Href.new_url == newurl).first():
            return "This short url is already used, try another one"
        href = Href(url, newurl)
        db.session.add(href)
        db.session.commit()
        return newurl
    else:
        return db.session.query(Href.new_url).filter(Href.url == url).scalar()


def return_url(url):
    res = db.session.query(Href.url).filter(Href.new_url == url)
    if not res.first():
        return "No such url"
    return res.scalar()