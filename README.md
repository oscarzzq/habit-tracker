# Flask Habit Tracker
A full-stack web application built with Python and Flask that allows users to create, track, and manage their personal habits. This project was developed as a final project for Harvard's CS50 course.

**Live Demo**: https://habit-tracker-oscar.onrender.com/

**Video Walkthrough**: https://youtu.be/o_7K_6X4BiI

## Description
This web-based habit tracker provides a simple and intuitive interface for users to monitor their daily routines and personal growth. Users can register for an account, create custom habits, and log their daily progress as a success, failure, or skip. The application features a persistent database to store all user data, ensuring a personalized experience across sessions. The front-end is designed to be clean and responsive, with color-coded habits for easy visual tracking.

## Features
* **User Authentication:** Secure user registration and login system with password hashing.

* **Habit Management (CRUD):** Users can Create, Read, Update, and Delete their habits.

* **Daily Logging:** Log daily progress for each habit as a "Success," "Failure," or "Skip."

* **Habit Archiving:** Move completed or paused habits to an archive to keep the main dashboard clean, with the option to delete them permanently.

* **Persistent Data:** User accounts, habits, and progress logs are stored in a SQLite database.

* **Dynamic Interface:** The dashboard is dynamically rendered based on the user's data, with color-coded entries for each habit.

## Technologies Used
* **Back-End:** Python, Flask

* **Database:** SQLite

* **Front-End:** HTML, CSS, Bootstrap

* **Deployment:** Gunicorn, Render

## How to Run Locally
To run this project on your local machine, please follow these steps:

1. Clone the repository:

git clone https://github.com/oscarzzq/habit-tracker.git

2. Navigate into the project directory:

cd habit-tracker

3. Install the required dependencies:

pip install -r requirements.txt

4. Run the application:

flask run

5. Open your browser and navigate to http://127.0.0.1:5000.

