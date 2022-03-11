from flask import render_template
from app import app
from .request import get_movies,get_movie



@app.route('/')
def index():

  # Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = "Home - Welcome to Night'sWatch"
    # Getting movie
    movie = get_movie
    return render_template('index.html', title = title,popular = popular_movies)


@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html',title = title,movie = movie)
