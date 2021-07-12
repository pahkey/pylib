import sqlite3
import time


def with_cursor(original_func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('blog.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        rv = original_func(c, *args, **kwargs)
        conn.commit()
        conn.close()
        return rv
    return wrapper


@with_cursor
def get_blog_list(c):
    c.execute("SELECT * FROM blog")
    return c.fetchall()


@with_cursor
def add_blog(c, subject, content):
    c.execute("INSERT INTO blog (subject, content, date) VALUES (?, ?, ?)",
        (subject, content, time.strftime('%Y%m%d')))


@with_cursor
def read_blog(c, _id):
    c.execute("SELECT * FROM blog WHERE id=?", (_id,))
    return c.fetchone()


@with_cursor
def modify_blog(c, _id, subject, content):
    c.execute("UPDATE blog SET subject=?, content=? WHERE id=?",
        (subject, content, _id))


@with_cursor
def remove_blog(c, _id):
    c.execute("DELETE FROM blog WHERE id=?", (_id,))
