from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
from datetime import datetime
import sqlite3

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

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

# @app.route('/')
# def index():
#     conn = sqlite3.connect('diary.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT id, date, content FROM notes ORDER BY date DESC')
#     notes = cursor.fetchall()
#     conn.close()
#     return render_template('index.html', notes=notes)

@app.route('/getNotes', methods=['GET'])
def get_notes():
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, date, content FROM notes ORDER BY date DESC')
    notes = cursor.fetchall()
    conn.close()
    
    def convert_bytes(item):
        if isinstance(item, bytes):
            return item.decode('utf-8')
        return item
    
    notes_serializable = [{'id': id, 'date': date, 'message': convert_bytes(message)} for id, date, message in notes]
    return jsonify(notes_serializable)

@app.route('/new', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        print(request.json["message"])
        content = request.json["message"]
        date = datetime.now().strftime('%Y-%m-%d')
        conn = sqlite3.connect('diary.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (date, content) VALUES (?, ?)', (date, content))
        conn.commit()
        conn.close()
        return redirect(url_for('new_note')) # not sure what to return here
    return "wrong place!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
