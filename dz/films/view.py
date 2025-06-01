def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output
        return wrap
    return wrapper


class UserInterface:

    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        # print("Редактирование данных каталога фильмов".center(50, "="))
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - просмотр каталога фильмов"
             "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_title("Добавление фильма: ")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        # print("Добавление фильма: ".center(50, "="))
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
            # print("=" * 50)
        return dict_film

    @add_title("Список фильмов: ")
    def show_all_films(self, films):
        # print("Список фильмов: ".center(50, "="))
        for ind, film in enumerate(films, 1):
            print(f"{ind}.{film}")
            # print("=" * 50)



