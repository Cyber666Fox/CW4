

from sqlalchemy import Column, String, Integer, Float, ForeignKey

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)

class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)

class Movies(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), unique=False, nullable=False)
    description = Column(String(100), unique=False, nullable=False)
    trailer = Column(String(100), unique=False, nullable=False)
    year = Column(Integer , nullable=False)
    rating = Column(Float , nullable=False)
    genre_id = Column(Integer, ForeignKey(f"{Genre.__tablename__}.id") , nullable=False)
    director_id = Column(Integer, ForeignKey(f"{Director.__tablename__}.id") , nullable=False)
    genre = relationship ('Genre')
    director = relationship ('Director')

class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), unique=True, nullable=False)
    surname = Column(String(100), unique=True, nullable=False)
    favourite_genre = Column(Integer, ForeignKey(f"{Genre.__tablename__}.id") , nullable=False)
    genre = relationship ('Genre')
  