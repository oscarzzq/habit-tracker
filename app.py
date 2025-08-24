import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///habits.db")
# Create tables if they don't exist
db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL,
        hash TEXT NOT NULL
    )
""")

db.execute("""
    CREATE TABLE IF NOT EXISTS habit (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        habit TEXT NOT NULL,
        times INTEGER,
        fails INTEGER,
        skips INTEGER,
        type TEXT,
        color TEXT,
        stime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
""")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user = session["user_id"]
    habits = db.execute("SELECT habit, stime, times, fails, skips, color FROM habit WHERE user_id = ? AND type = ?", user, 'current')
    return render_template("index.html", habits=habits)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("Please enter a username.")

        if not request.form.get("password"):
            return apology("Please enter a password.")

        if request.form.get("confirmation") == None:
            return apology("Please enter your password again.")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("The two passwords do not match.")

        passw = generate_password_hash(request.form.get("password"))
        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), passw)
            # id = db.execute("SELECT id FROM users WHERE username = ?", request.form.get("username"))
            # session["user_id"] = id
            return redirect("/login")

        except:
            return apology("Username is already taken, please change.")

    if request.method == "GET":
        return render_template("register.html")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        if not request.form.get("name"):
            return apology("Invalid name")
        else:
            name = request.form.get('name').replace(" ", "_")
        try:
            db.execute("INSERT INTO habit (user_id, habit, times, fails, skips, type, color) VALUES (?, ?, 0, 0, 0, 'current', ?)", session['user_id'], name, request.form.get("color"))
        except:
            return apology("Invalid color")
        return redirect("/")

@app.route("/archive", methods=["GET", "POST"])
@login_required
def archive():
    if request.method == "GET":
        habits = db.execute("SELECT habit FROM habit WHERE user_id = ? AND type = 'current'", session["user_id"])
        return render_template("archive.html", habits=habits)
    if request.method == "POST":
        if request.form.get("mode") == None:
            return apology("Invalid action")
        elif request.form.get("mode") == "archive":
            try:
                db.execute("UPDATE habit SET type = 'archive' WHERE user_id = ? AND habit = ?", session["user_id"], request.form.get("habit"))
            except:
                return apology("Invalid habit")
            return redirect("/")
        elif request.form.get("mode") == "delete":
            try:
                db.execute("DELETE FROM habit WHERE user_id = ? AND habit = ?", session["user_id"], request.form.get("habit"))
            except:
                return apology("Invalid habit")
            return redirect("/")


@app.route("/archived")
@login_required
def archived():
    habits = db.execute("SELECT habit, stime, times, fails, skips, color FROM habit WHERE user_id = ? AND type = 'archive'", session["user_id"])
    return render_template("archived.html", habits=habits)

@app.route("/log", methods=["GET", "POST"])
@login_required
def log():
    if request.method == "GET":
        habits = db.execute("SELECT habit FROM habit WHERE user_id = ? AND type = 'current'", session["user_id"])
        return render_template("log.html", habits=habits)
    if request.method == "POST":
        if request.form.get("habit") == None:
            return apology("Invalid habit")
        elif request.form.get("action") == None:
            return apology("Invalid action")
        elif not request.form.get("times"):
            return apology("Invalid number")
        elif int(request.form.get("times")) <= 0:
            return apology("Invalid number")
        else:
            if request.form.get("action") == 'succeed':
                original = db.execute("SELECT times FROM habit WHERE user_id = ? AND habit = ?", session["user_id"], request.form.get('habit'))[0]['times']
                final = original + int(request.form.get('times'))
                db.execute("UPDATE habit SET times = ? WHERE habit = ? AND user_id = ?", final, request.form.get('habit'), session["user_id"])
                return redirect("/")
            elif request.form.get("action") == 'fail':
                original = db.execute("SELECT fails FROM habit WHERE user_id = ? AND habit = ?", session["user_id"], request.form.get('habit'))[0]['fails']
                final = original + int(request.form.get('times'))
                db.execute("UPDATE habit SET fails = ? WHERE habit = ? AND user_id = ?", final, request.form.get('habit'), session["user_id"])
                return redirect("/")

            elif request.form.get("action") == 'skip':
                original = db.execute("SELECT skips FROM habit WHERE user_id = ? AND habit = ?", session["user_id"], request.form.get('habit'))[0]['skips']
                final = original + int(request.form.get('times'))
                db.execute("UPDATE habit SET skips = ? WHERE habit = ? AND user_id = ?", final, request.form.get('habit'), session["user_id"])
                return redirect("/")


@app.route("/tem")
def tem():
    return render_template('tem.html')
