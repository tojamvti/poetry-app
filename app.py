from flask import Flask, render_template, abort
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "mybookdb",
    "user": "postgres",
    "password": "haaslo",
    "host": "127.0.0.1",
    "port": "5433"
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM chapters ORDER BY id;")
    chapters = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", chapters=chapters)

@app.route("/chapter/<int:id>")
def chapter(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT title, content FROM chapters WHERE id = %s;", (id,))
    chapter = cur.fetchone()
    cur.close()
    conn.close()
    if chapter is None:
        abort(404)
    title, content = chapter
    return render_template("chapter.html", title=title, content=content)

if __name__ == "__main__":
    app.run(debug=True)
