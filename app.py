from flask import Flask, request, redirect, render_template, session
from book import Book
from BookRepository import BookRepository
from database_connection import DatabaseConnection
from film import Film
from FilmRepository import FilmRepository
from user import User
from user_repository import UserRepository
from login_required import login_required


# instantiate a Flask app object
app = Flask(__name__)
app.secret_key = "some_really_secret_key"

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

# new route"
@app.route('/books', methods=['GET'])
def books():
    db = DatabaseConnection()
    db.connect()
    repo = BookRepository(db)
    books = repo.all()
    return render_template("books.html", books = books)


#iteration 2: add route for team:
@app.route('/team', methods=['GET'])
def get_team():
    team = ["Dorothy", "Rose", "Blanche", "Sophia"]
    return render_template("team.html", team=team)


# adding new route for authors:
@app.route('/authors', methods=['GET'])
def authors():
    return [
    {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
    },
    {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
    },
    {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
    },
    {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
    }
]

# adding html route
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


# adding function to get reading quotes:
@app.route('/quotes', methods=['GET'])
def quotes():
    return render_template("quotes.html")

# Adding first POST for /books:

@app.route('/books', methods=['POST'])
@login_required
def create_book():
    book_details = request.form #changed from request.json
    db = DatabaseConnection()
    db.connect()
    repo = BookRepository(db)
    book = Book(None, book_details["title"], book_details["author"])
    repo.create(book)
    print(book_details)
    return redirect("/books")

# route to GET /films
@app.route('/films', methods=['GET'])
def films():
    db = DatabaseConnection()
    db.connect()
    repo = FilmRepository(db)
    films = repo.all()
    return render_template("films.html", films=films)

# creating route to POST /films:
@app.route('/films', methods= ['POST'])
def create_film():
    film_details= request.form
    db = DatabaseConnection()
    db.connect()
    repo = FilmRepository(db)
    film = Film(None, film_details["title"], film_details["genre"], film_details["release_date"])
    repo.create(film)
    return redirect("/films")

# route to GET /users:
@app.route('/users', methods=['GET'])
def get_users_list():
    db = DatabaseConnection()
    db.connect()
    repo = UserRepository(db)
    users= repo.all()
    return render_template("users.html", users=users)

# route for sign-up form: 
@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("users.html")

# route to create users:
@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details= request.form
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/users")

#route for login form:
@app.route('/sessions/new', methods=['GET'])
def get_login_form():
    return render_template("login_form.html")

# route to POST /sessions:
@app.route('/sessions', methods=['POST'])
def submit_to_login_form():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    username = request.form["username"]
    password = request.form["password"]

    user = user_repository.find_by_username(username)

    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)