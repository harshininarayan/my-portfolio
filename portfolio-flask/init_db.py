import sqlite3

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect('contact.db')
cursor = conn.cursor()

# Create the messages table
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("✅ Database and 'messages' table created successfully.")
