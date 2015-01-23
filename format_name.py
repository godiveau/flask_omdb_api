# -*- coding: utf-8 -*-
import unicodedata

def format_name(movie_name):
    movie_name = movie_name.strip().replace(" ","+")
    return u"%s" % (movie_name.encode('utf-8'))
