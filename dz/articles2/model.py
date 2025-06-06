class Article:
    def __init__(self, title, genre, producer, year_release, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.producer = producer
        self.year_release = year_release
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} " "Режиссер: " f"{self.producer}" "Актеры: " f"{self.actors}"


class ArticleModel:
    def __init__(self):
        self.articles = {}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

