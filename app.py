from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
connection = mysql.connector.connect(
    host='mysql.railway.internal',  # Replace with your MySQL host
    user='root',  # Replace with your MySQL username
    password='sApkVSAVJiGRsvCUCIFiqfwZjHhIAqHB',  # Replace with your MySQL password
    database='railway',  # Replace with your database name
    auth_plugin='mysql_native_password',
    connection_timeout=10000  # Increase the timeout to 60 seconds
)

@app.route('/')
def index():
    return render_template('index.html')

# Step 5: Implement the Queries
@app.route('/login', methods=['POST'])
def login():
    screen_name = request.form['screen_name']
    cursor = connection.cursor()
    query = '''
    SELECT Problem.name, Contest.name
    FROM Submission
    JOIN Problem ON Submission.contestId = Problem.contestId AND Submission.problemIndex = Problem.problemIndex
    JOIN Contest ON Submission.contestId = Contest.id
    WHERE Submission.handle = %s
    '''
    cursor.execute(query, (screen_name,))
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names, screen_name=screen_name)

@app.route('/show_writer', methods=['POST'])
def show_writer():
    screen_name = request.form['screen_name']
    cursor = connection.cursor()
    query = '''
    SELECT Contest.name
    FROM Contest_Writer
    JOIN Contest ON Contest_Writer.contestId = Contest.id
    WHERE Contest_Writer.handle = %s
    '''
    cursor.execute(query, (screen_name,))
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names, screen_name=screen_name)

@app.route('/problems_by_tag', methods=['POST'])
def problems_by_tag():
    tag = request.form['tag']
    cursor = connection.cursor()
    query = '''
    SELECT Problem.name
    FROM Problem_Tag
    JOIN Problem ON Problem_Tag.contestId = Problem.contestId AND Problem_Tag.problemIndex = Problem.problemIndex
    WHERE Problem_Tag.tagName = %s
    '''
    cursor.execute(query, (tag,))
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names, tag=tag)

@app.route('/top_languages', methods=['GET'])
def top_languages():
    cursor = connection.cursor()
    query = '''
    SELECT programmingLanguage, AVG(timeConsumedMillis) AS avg_time, AVG(memoryConsumedBytes) AS avg_memory
    FROM Submission
    GROUP BY programmingLanguage
    ORDER BY avg_time ASC, avg_memory ASC
    LIMIT 5
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names)

@app.route('/top_users_streak', methods=['GET'])
def top_users_streak():
    cursor = connection.cursor()
    query = '''
    SELECT handle, streak, numberOfProblemsSolved
    FROM User
    ORDER BY streak DESC, numberOfProblemsSolved DESC
    LIMIT 10
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names)

@app.route('/top_users_score', methods=['GET'])
def top_users_score():
    cursor = connection.cursor()
    query = '''
    SELECT Contest_Standing.handle, SUM(Contest_Standing.score) AS total_score
    FROM Contest_Standing
    JOIN Contest ON Contest_Standing.contestId = Contest.id
    WHERE Contest.division IN ('Div. 1', 'Div. 2')
    GROUP BY Contest_Standing.handle
    ORDER BY total_score DESC
    LIMIT 10
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names)

@app.route('/top_organizations', methods=['GET'])
def top_organizations():
    cursor = connection.cursor()
    query = '''
    SELECT organization, country, AVG(rating) AS avg_rating
    FROM User
    WHERE rating IS NOT NULL
    GROUP BY organization, country
    ORDER BY avg_rating DESC
    LIMIT 5
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names)

@app.route('/top_users_frequency', methods=['GET'])
def top_users_frequency():
    cursor = connection.cursor()
    query = '''
    SELECT User.handle, COUNT(Contest_Participant.contestId) / User.registrationPeriodDays AS participation_frequency
    FROM Contest_Participant
    JOIN User ON Contest_Participant.handle = User.handle
    GROUP BY User.handle, User.registrationPeriodDays
    ORDER BY participation_frequency DESC
    LIMIT 5
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names)

@app.route('/top_auc_users', methods=['GET'])
def top_auc_users():
    cursor = connection.cursor()
    query = '''
    SELECT handle, rating
    FROM User
    WHERE organization = 'AUC'
    ORDER BY rating DESC
    LIMIT 10
    '''
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names)

@app.route('/top_egypt_problems', methods=['GET'])
def top_egypt_problems():
    cursor = connection.cursor()
    query = '''
    SELECT Problem.name, COUNT(Submission.handle) AS attempts
    FROM Submission
    JOIN Problem ON Submission.contestId = Problem.contestId AND Submission.problemIndex = Problem.problemIndex
    JOIN User ON Submission.handle = User.handle
    WHERE User.country = %s
    GROUP BY Problem.name
    ORDER BY attempts DESC
    LIMIT 5
    '''
    cursor.execute(query, ('Egypt',))
    data = cursor.fetchall()
    column_names = [i[0] for i in cursor.description]  # Get column names
    cursor.close()
    return render_template('result.html', data=data, column_names=column_names)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the PORT from the environment, default to 5000
    app.run(host="0.0.0.0", port=port)
