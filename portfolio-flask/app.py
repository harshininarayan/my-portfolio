# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        conn = sqlite3.connect('contact.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
                       (name, email, message))
        conn.commit()
        conn.close()
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/admin/messages')
def admin_messages():
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, message, submitted_at FROM messages ORDER BY submitted_at DESC")
    messages = cursor.fetchall()
    conn.close()
    return render_template('admin_msg.html', messages=messages)


if __name__ == '__main__':
    app.run(debug=True)

