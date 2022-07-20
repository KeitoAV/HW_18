from flask import request
from flask_restx import Namespace, Resource

from app.container import movie_service
from app.dao.model.movie import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        filters = {
            'director_id': request.args.get('director_id', type=int),
            'genre_id': request.args.get('genre_id', type=int),
            'year': request.args.get('year', type=int)
        }
        all_movies = movie_service.get_filter_data(filters)

        if not all_movies:
            return "в БД нет фильмов по заданным параметрам", 404

        return movies_schema.dump(all_movies), 200

    def post(self):
        data = movie_schema.load(request.json)
        movie = movie_service.create(data)
        return f"В БД добавлен фильм с ID - {movie.id}", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)

        if not movie:
            return f"Фильм с ID - {mid} отсутствует в БД", 404

        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        data = request.json
        data["id"] = mid
        movie_service.update(data)

        return f"Фильм с ID - {mid} успешно обновлён", 201

    def delete(self, mid: int):
        movie = movie_service.get_one(mid)
        if not movie:
            return f"Фильм с ID - {mid} отсутствует в БД", 404

        movie_service.delete(mid)
        return f"Фильм с ID - {mid} удален", 201
