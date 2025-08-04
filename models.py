import psycopg2

def get_connection():
    return psycopg2.connect(
        host="postgres-db",    # match your Docker container name
        port=5432,
        user="myuser",
        password="mypassword",
        database="mydb"
    )

def get_poems():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM poems ORDER BY id")
    poems = cur.fetchall()
    cur.close()
    conn.close()
    return poems

def get_chapters():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content, chapter_number FROM chapters ORDER BY chapter_number")
    chapters = cur.fetchall()
    cur.close()
    conn.close()
    return chapters
