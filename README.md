# Habit Tracker by Oscar Zhang
#### Video Demo: https://youtu.be/o_7K_6X4BiI
#### Description:
My final project is a habit tracker which allows users to add their own habits, log experiences, and archive habits when the habit is completely developed and requires no more recording. When users are logging their experiences they can choose to count them as successes, failures, or skips. Also, when they want to archive the habit they can choose between archiving it and deleting it. I used python, HTML, CSS, and bootstrap's library to help me develop the web application.

In my helpers.py document, I used CS50's provided code for the finance problem set which you can visit here https://cs50.harvard.edu/x/2022/psets/9/finance/. The apology function turns your apology to the user (which is a text) into a meme with a picture format, I chose to use this function because I think instead of directly using an error message, using this meme format will make the user happier when using my website, so they will use my website more frequently. I also find the login required function very helpful, because almost everything that my website can do needs the user to be logged in.

In my app.py, is where most of my python code lies and it is like the "brain" for my program. In my app.py I define all the paths of my website, processes the information given from the HTML, and also give information to HTML files.

My habits.db is where all my data of the users and their habits are stored, it is a sqlite3 database. There are two tables that I designed called users and habit, the first stores all the user's information (their password hash, id, username), the second stores each habit's information (the user_id, id, time created, successes, fails, skips, habit name, type, color).

Using my add.html combined with my app.py, helpers.py, and habits.db, I can add habits for my users. They can choose their habit's name and they can choose a color that will be displayed on the homepage.

Using my apology.html combined with helpers.py and app.py, I can render an apology message when something goes wrong in my web application.

Using my archive.html combined with app.py, helpers.py, and habits.db, the user can choose to archive or delete some of their habits. I made two options of archive and delete because when a user develops a habit very well and does not need to record it anymore, they can archive it. This way afterward they can check it again through the "view archived" page to see the previous habits that they have developed and check if they are still following the habit. However, if the user just made a mistake and created a habit they don't need, they can delete it permanently, because they do not need to see it again.

Using my archived.html combined with app.py, habits.db, and helpers.py, I can show a list of the user's archived habits to them. They can see when they started the habit, the habit's name, and how many failures/successes/skips they had with the habit.

Using my index.html combined with apps.py, helpers.py, and habits.db, I can see a list of the habits that I am currently developing. It can be shown in different colors according to the color selected by the user when they created the habit, the color of the buttons also changes with the color of the habits. The user can see through a table the habits' names, their time created, and their successes/failures/skips. There are also buttons in each row that links to a page that logs the habit and a page that archives/delete the habits.

My layout.html is a layout of my basic HTML that my other HTML files are based on. My other HTML files expand this template so I can have less code to write. Some parts of the layout.html are based on a previous CS50 problem set called finance https://cs50.harvard.edu/x/2022/psets/9/finance/, other parts are from bootstrap5 https://getbootstrap.com.

Using my log.html combined with my apps.py, helpers.py, and habits.db, I can let users log experiences of successes, failures, and skips. I developed different logs of successes, failures, and skips to give users more choices. Also, sometimes people are forced to depart from their habits because of reasons that they cannot control; they cannot be counted as failures nor successes. Therefore, I developed another option of skipping in my habit tracker.

Using my login.html combined with apps.py, habits.db, and helpers.py, users can log in to their accounts to see their own habits and records.

Using my register.html combined with apps.py, habits.db, and helpers.py, users can register their own new accounts.

In my styles.css I changed the color of my project's title color from black to light blue.