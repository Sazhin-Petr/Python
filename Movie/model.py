import pickle
import os.path
from zoneinfo import reset_tzpath

class Movie:
    def __init__(self, title, genre, producer, age, time, studio, actors):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.age = age
        self.time = time
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f'{self.title} ({self.producer})'


class MovieModel:
    def __init__(self):
        self.db_name = 'db.txt'
        self.Movie = self.load_data()

    def add_movies(self,dict_movie):
        movie = Movie(*dict_movie.values())
        self.Movie[movie.title] = movie

    def get_all_movies(self):
        return self.Movie.values()

    def get_single_movie(self, user_title):
        movie = self.Movie[user_title]
        dict_movie = {
            'название': movie.title,
            'жанр': movie.genre,
            'режиссер': movie.producer,
            'год выпуска': movie.age,
            'длительность': movie.time,
            'студия': movie.studio,
            'актеры': movie.actors,
        }
        return dict_movie

    def remove_movie(self, user_movie):
        return self.Movie.pop(user_movie)

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.Movie, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)

        else:
            return dict()