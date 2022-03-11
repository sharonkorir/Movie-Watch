class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count,homepage):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.homepage = homepage

class Trailer:
    '''
    Trailer class to define trailer objects
    '''
    def __init__(self,id,name,key,type):
        self.id = id
        self.name = name
        self.key = key
        self.type = type