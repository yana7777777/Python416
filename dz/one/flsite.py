from flask import Flask, render_template, request


app = Flask(__name__)

menu = [
    {"name": "Главная", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Обратная связь", "url": "contact"}
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="О нас", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)

