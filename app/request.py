import urllib.request,json
from .models import Movie, Trailer

# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']


def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results

    
def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        homepage =movie_item.get('homepage')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count,homepage)
            movie_results.append(movie_object)

    return movie_results

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')
            homepage = movie_details_response.get('homepage')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count, homepage)

    return movie_object

def email_subscription(user_email, user_group_email, mail_gun_api_key):
    pass

def select_genre(genre_name):
    get_genre_url = 'https://api.themoviedb.org/3/genre/movie/list?api_key={}'.format(api_key,genre_name)
    with urllib.request.urlopen(get_genre_url) as url:
        genre_data = url.read()
        get_genre_response = json.loads(genre_data)

        get_genre_results = None

        if get_genre_response['genres']:
            genre_list = get_genre_response['genres']
            get_genre_results = process_results(genre_list)


    return get_genre_results

def show_trailer(id):
    '''
    Function to get movie trailer key terms and search on youtube
    '''
    trailer_url = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}'.format(
        id, api_key)

    with urllib.request.urlopen(trailer_url) as url:
        trailer_data = url.read()
        trailer_response = json.loads(trailer_data)

        movie_trailer_results = None
        if trailer_response['results']:
            trailer_list = trailer_response['results']
            movie_trailer_results = process_trailer_results(trailer_list)

    return movie_trailer_results


def process_trailer_results(trailer_list):
    trailer_results = []
    for trailer_item in trailer_list:
        id = trailer_item.get('id')
        name = trailer_item.get('name')
        key = trailer_item.get('key')
        type = trailer_item.get('type')

        trailer_object = Trailer(id, name, key,type)
        trailer_results.append(trailer_object)

    return trailer_results