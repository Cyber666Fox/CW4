from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссеры', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Тейлор Шеридан'),
})

movie: Model = api.model('Фильмы', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Чикаго'),
    'description': fields.String(required=True, max_length=250, example='Чикаго'),
    'trailer': fields.String(required=True, max_length=100, example='Чикаго'),
    'year' : fields.Integer(required=True, example= 2015),
    'rating' : fields.Float(required=True, example= 7.0),
    'genre_id' : fields.Nested(genre),
    'director_id' : fields.Nested(director),
    })

user: Model = api.model('Пользователи', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='Alex@gmail.com'),
    'password': fields.String(required=True, max_length=100, example='Al123ex'),
    'name': fields.String(required=True, max_length=100, example='Alexendr'),
    'sername' : fields.String(required=True, max_length=100, example='Kupriyanov'),
    'genre ' : fields.Nested(genre),
})