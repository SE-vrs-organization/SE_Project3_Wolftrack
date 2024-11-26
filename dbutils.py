"""
MIT License

Copyright (c) 2023 Shonil B, Akshada M, Rutuja R, Sakshi B

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import sqlite3

def create_tables(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS client (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            usertype TEXT NOT NULL
        )
    """
    )
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        location TEXT,
        job_position TEXT,
        salary INTEGER,
        status TEXT
    )
    """
    )
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS bookmarked_jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        location TEXT,
        job_position TEXT,
        salary INTEGER,
        contract_time TEXT,
        user_id INTEGER
    )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES client (id)
        )
    """
    )

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resume_review (
        user_id TEXT PRIMARY KEY,
        resume TEXT,
        comments TEXT
    )
    """)
    conn.commit()
    conn.close()


def add_client(value_set, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    print(value_set)
    # Inserting rows into the 'client' table
    cursor.execute(
        "INSERT INTO client (name, username, password, usertype) VALUES (?, ?, ?, ?)",
        value_set,
    )
    conn.commit()
    conn.close()


def find_user(data, db):
    conn = sqlite3.connect(db)
    print("Data==>", data)
    cursor = conn.cursor()
    # Querying the 'client' table
    cursor.execute("SELECT * FROM client where username ='" + str(data) + "'")
    rows = cursor.fetchone()
    conn.close()
    print("rowsss->>>", rows)
    return rows


def add_job(data, db):
    conn = sqlite3.connect(db)
    print("Data==>", data)
    cursor = conn.cursor()
    # Inserting rows into the 'jobs' table
    cursor.execute(
        "INSERT INTO jobs (company_name, location, job_position, salary, status) VALUES (?, ?, ?, ?, ?)",
        data,
    )
    conn.commit()
    conn.close()


def get_job_applications(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()  # Use fetchall() to get all rows
    conn.close()
    print("rows ->>>", rows)
    return rows


def update_job_application_by_id(company, location, jobposition, salary, status, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Update the 'jobs' table based on jobid
    cursor.execute(
        "UPDATE jobs SET company_name=?, location=?, job_position=?, salary=?, status=? WHERE company_name=?",
        (company, location, jobposition, salary, status, company),
    )

    conn.commit()
    conn.close()


def delete_job_application_by_company(company_name, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Delete the job application from the 'jobs' table based on the company name
    cursor.execute("DELETE FROM jobs WHERE company_name=?", (company_name,))

    conn.commit()
    conn.close()


def get_job_applications_by_status(db, status):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE status = ?", (status,))
    rows = cursor.fetchall()  # Use fetchall() to get all rows
    conn.close()
    print("rows ->>>", rows)
    return rows


def add_bookmark(db, job, user):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    # Inserting rows into the 'client' table
    cursor.execute(
        """
            INSERT INTO bookmarked_jobs (company_name, location, job_position, salary, contract_time, user_id) 
            VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            job["company_name"],
            job["location"],
            job["job_position"],
            job["salary"],
            job["contract_time"],
            user,
        ),
    )
    conn.commit()
    conn.close()


def get_bookmarks(db, user):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT company_name, location, job_position, salary, contract_time FROM bookmarked_jobs
            WHERE user_id = ?
        """,
        (user,),
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_event(db, event, user_id):
    print("Db event: ",event)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO events (title, description, start_date, end_date, user_id)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            event["title"],
            event["description"],
            event["start_date"],
            event["end_date"],
            user_id,
        ),
    )
    conn.commit()
    conn.close()

def get_user_events(db, user_id):
    print("User id: ",user_id)
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, title, description, start_date, end_date FROM events WHERE user_id = ? ORDER BY start_date
        """,
        (user_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

# def update_event(db, event_id, event_data):
#     conn = sqlite3.connect(db)
#     cursor = conn.cursor()
#     cursor.execute(
#         """
#         UPDATE events SET title = ?, description = ?, start_time = ?, end_time = ?
#         WHERE id = ?
#         """,
#         (event_data["title"], event_data.get("description"), event_data["start_time"], event_data["end_time"], event_id),
#     )
#     conn.commit()
#     conn.close()
#
# def delete_event(db, event_id):
#     conn = sqlite3.connect(db)
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM events WHERE id = ?", (event_id,))
#     conn.commit()
#     conn.close()



def add_resume(db,filepath, user):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Inserting rows into the 'resume_review' table
    cursor.execute(
        """
            INSERT OR REPLACE INTO resume_review (user_id, resume, comments) 
            VALUES (?, ?, ?)
        """,
        (
            user,
            filepath,
            None,
        ),
    )
    conn.commit()
    conn.close()


def get_resume(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * FROM resume_review
        """,
    )
    rows = cursor.fetchall()
    print(rows)
    conn.close()
    return rows

def add_comments(db,comments,user):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
        """
            UPDATE resume_review 
            SET comments = ? 
            WHERE user_id = ?
        """,
        (
            comments,
            user,
        )
    )
    conn.commit()
    conn.close()

def get_comments(db,user):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT resume, comments FROM resume_review
        WHERE user_id = ?
    """, (user,))
    data = cursor.fetchall()
    conn.close()
    return data
