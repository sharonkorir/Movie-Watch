from flask import render_template
from . import main
from ..request import get_movies,get_movie,show_trailer



@main.route('/', methods=['GET','POST'])
def index():

  # Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = "Home - Welcome to MovieWatch"
    # Getting movie
    movie = get_movie
    return render_template('index.html', title = title,popular = popular_movies)


@main.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    trailers = show_trailer(id)

    return render_template('movie.html',title = title,movie = movie, trailer = trailers)
