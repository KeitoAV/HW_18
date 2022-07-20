from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def get_filter_data(self, filters: dict):
        movies = self.session.query(Movie)

        if filters['director_id']:
            movies = movies.filter(Movie.director_id == filters['director_id'])
        if filters['genre_id']:
            movies = movies.filter(Movie.genre_id == filters['genre_id'])
        if filters['year']:
            movies = movies.filter(Movie.year == filters['year'])

        return movies.all()

    def delete(self, mid):
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()
