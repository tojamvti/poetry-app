from flask import Flask, render_template
import psycopg2
import os
from dotenv import load_dotenv

# Wczytaj zmienne środowiskowe
load_dotenv()

app = Flask(__name__)

# Funkcja do połączenia z bazą danych
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM poems;')
    poems = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', poems=poems)

if __name__ == '__main__':
    app.run(debug=True)
