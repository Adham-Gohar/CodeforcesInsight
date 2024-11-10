# CodeforcesInsight

## Overview
CodeforcesInsight is a Flask-based web application that allows users to explore and analyze data related to competitive programming contests on Codeforces. This application connects to a MySQL database populated with data from Codeforces, providing various insights, such as user statistics, contest standings, problem analysis, and much more. The goal of this project is to enhance the accessibility of competitive programming data and provide meaningful insights for users, writers, and teams.

## Features
- **User Participation**: View all the contests and problem sets attempted by a given user.
- **Writer Contributions**: Show all contests authored by a specific writer.
- **Problem Analysis**: Filter and view all problems based on specific tags.
- **Top Languages**: Analyze the most efficient programming languages used to solve problem sets.
- **Top Users and Teams**: View rankings of users based on their streaks, problems solved, and contest scores.
- **Organization Insights**: View the top organizations by ratings and user performance in contests.

## Application URL
The live application can be accessed here: [CodeforcesInsight App](codeforcesinsight-production-31f2.up.railway.app)

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/CodeforcesInsight.git
   cd CodeforcesInsight
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Download the SQL dump from the following link: [Codeforces SQL Dump](https://drive.google.com/drive/folder-link)
   - Import the SQL dump to your MySQL server:
     ```bash
     mysql -u your_user -p your_database < codeforces.sql
     ```

5. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add the following variables:
   ```env
   DB_HOST=your_mysql_host
   DB_PORT=3306
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_NAME=your_mysql_database
   PORT=5000
   ```

6. **Run the Application**:
   ```bash
   python app.py
   ```

7. **Access the Application**:
   The application will be available at `http://localhost:5000`.

## Deployment
This project is deployed on [Railway](https://railway.app/). To deploy it yourself:
- Link your GitHub repository to Railway.
- Set up a new project and add MySQL as a plugin.
- Update environment variables using Railway's interface.

## Usage
- Visit the home page to see available queries.
- Enter required information (such as user handle or tag) and click the buttons to execute queries.
- The results will be displayed in a user-friendly format.

## Project Structure
- **app.py**: The main Flask application file that handles routes and database connections.
- **templates/**: HTML templates for the frontend (`index.html`, `result.html`).
- **static/**: Static files such as CSS, images, and JavaScript.
- **requirements.txt**: List of Python dependencies required for the project.

## Database Schema
The application uses a MySQL database with the following tables:
- **User**: Stores user information such as handle, rating, and participation details.
- **Contest**: Stores contest information.
- **Problem**: Stores problem details used in contests.
- **Submission**: Tracks user submissions to problems.
- **Tags, Contest Writer, Contest Participant, Contest Standing, Problem Tag**: Relational tables for metadata.

## Acknowledgements
- **Codeforces** for providing the data and API access.
- **Railway** for providing the hosting environment.

## Disclaimer
This project is for educational purposes only and is not affiliated with Codeforces.
