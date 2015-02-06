# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request
from format_name import *
import requests
import unicodedata

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def api_root():
    if request.method == 'POST':
        movie_name= format_name(request.form[u'movie_name'])
        url = "http://www.omdbapi.com/?t={0}&y=&plot=short&r=json".format(movie_name)
        omdb_request = requests.get(url)
        omdb_result = omdb_request.json()
        return render_template("index.html", movie_name=movie_name, omdb_request=omdb_result)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='192.168.56.102', port=8080, debug=True)
