# import sqlite3
#
#
# def display_messages():
#     try:
#         conn = sqlite3.connect('contact.db')
#         cursor = conn.cursor()
#
#         cursor.execute("SELECT id, name, email, message FROM messages")
#         rows = cursor.fetchall()
#
#         if not rows:
#             print("No messages found in the database.")
#         else:
#             print("\nContact Form Submissions:\n")
#             for row in rows:
#                 print(f"ID: {row[0]}")
#                 print(f"Name: {row[1]}")
#                 print(f"Email: {row[2]}")
#                 print(f"Message: {row[3]}")
#                 # print(f"Submitted At: {row[4]}")
#                 print("-" * 40)
#
#     except sqlite3.Error as e:
#         print("Database error:", e)
#
#     finally:
#         conn.close()
#
#
# if __name__ == "__main__":
#     display_messages()


import sqlite3

def display_messages():
    try:
        conn = sqlite3.connect('contact.db')
        cursor = conn.cursor()

        # Get column names in the 'messages' table
        cursor.execute("PRAGMA table_info(messages)")
        columns = [col[1] for col in cursor.fetchall()]

        # Build SELECT query based on existing columns
        select_columns = ['id', 'name', 'email', 'message']
        if 'submitted_at' in columns:
            select_columns.append('submitted_at')

        query = f"SELECT {', '.join(select_columns)} FROM messages"
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("No messages found in the database.")
        else:
            print("\nContact Form Submissions:\n")
            for row in rows:
                for idx, col in enumerate(select_columns):
                    print(f"{col.capitalize()}: {row[idx]}")
                print("-" * 40)

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()

if __name__ == "__main__":
    display_messages()
