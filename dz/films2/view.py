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
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
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

    @add_title("Ввод названия фильма:")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр фильма:")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} статьи - {film[key]}")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильма с названием {user_title} не существует")

    @add_title("Удаление фильма:")
    def remove_single_film(self, film):
        print(f"Фильм {film} - была удалена")

    @add_title("Сообщение об ошибке:")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")



