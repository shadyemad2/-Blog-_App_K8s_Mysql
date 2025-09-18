from flask import Flask, request, render_template_string
import mysql.connector
import os

app = Flask(__name__)


DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "bloguser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "userpass")
DB_NAME = os.getenv("DB_NAME", "blogdb")

# HTML template 
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Mini Blog</title>
</head>
<body>
    <h1>📝 Mini Blog App</h1>
    <form method="POST" action="/add">
        <textarea name="content" rows="4" cols="50" placeholder="Write your post..."></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
    <h2>Posts:</h2>
    <ul>
        {% for post in posts %}
            <li>{{ post[1] }} ({{ post[2] }})</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route("/", methods=["GET"])
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template_string(HTML, posts=posts)

@app.route("/add", methods=["POST"])
def add_post():
    content = request.form["content"]
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (content) VALUES (%s)", (content,))
    conn.commit()
    cursor.close()
    conn.close()
    return ("<p>Post added!</p><a href='/'>Back</a>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

