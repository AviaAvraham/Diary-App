from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('SELECT date, content FROM notes ORDER BY date DESC')
    notes = cursor.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

# @app.route('/new', methods=['GET', 'POST'])
# def new_note():
#     if request.method == 'POST':
#         content = request.form['content']
#         date = datetime.now().strftime('%Y-%m-%d')
#         conn = sqlite3.connect('diary.db')
#         cursor = conn.cursor()
#         cursor.execute('INSERT INTO notes (date, content) VALUES (?, ?)', (date, content))
#         conn.commit()
#         conn.close()
#         return redirect(url_for('index'))
#     return render_template('new_note.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
