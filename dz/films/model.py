class Film:
    def __init__(self, title, genre, producer, year_release, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year_release = year_release
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return "Фильм: " f"{self.title}, " "Режиссер: " f"{self.producer}, " " Актеры: " f"{self.actors}"


class FilmModel:
    def __init__(self):
        self.films = {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

