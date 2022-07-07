# A blog website with Flask and SQLite3
import sqlite3
from flask import Flask, g, render_template, request, redirect, url_for, flash
from contextlib import closing

# Create database and create table
def create_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Connect to database
def connect_db():
    return sqlite3.connect('blog.db')

# Create Flask application
app = Flask(__name__)
app.config.from_object(__name__)

# Create flask index handler
@app.route('/')
def index():
    return render_template('index.html')

# Create flask blog handler
@app.route('/blog')
def blog():
    with closing(connect_db()) as db:
        cur = db.execute('select title, text, id from entries order by id desc')
        entries = [dict(title=row[0], text=row[1], id=row[2]) for row in cur.fetchall()]
    return render_template('blog.html', entries=entries)

# Make new blog
@app.route('/new_entry', methods=['GET', 'POST'])
def new_entry():
    if request.method == 'POST':
        if not request.form['title'] or not request.form['text']:
            flash('Title and text are required.')
            return redirect(url_for('new_entry'))
        with closing(connect_db()) as db:
            db.execute('insert into entries (title, text) values (?, ?)',
                       [request.form['title'], request.form['text']])
            db.commit()
        flash('New entry was successfully posted.')
        return redirect(url_for('blog'))
    return render_template('new_entry.html')