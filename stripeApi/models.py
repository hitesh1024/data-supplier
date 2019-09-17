import sqlite3
import datetime


class function:

    def insert_into_database(cus_id, email):
        conn = sqlite3.connect('user.db', check_same_thread=False, timeout=20)
        c = conn.cursor()
        c.execute("INSERT INTO user Values(?,?)", (cus_id, email))
        conn.commit()
        c.close()
        conn.close()

    def search(email):
        # email = 'patsaurabh@gmail.com'
        conn = sqlite3.connect('user.db', check_same_thread=False, timeout=20)
        c = conn.cursor()
        c.execute("SELECT email FROM user WHERE email=?", (email,))
        data = c.fetchall()
        if len(data) == 0:
            conn.commit()
            c.close()
            conn.close()
            return None
        else:
            data1 = data[0]
            conn.commit()
            c.close()
            conn.close()
            return data1[0]

