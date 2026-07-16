from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():

    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT", 3306))
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()
    headings = [i[0] for i in cursor.description]

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        rows=rows,
        headings=headings
    )


@app.route("/teachers")
def teachers():

    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT", 3306))
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM teachers")

    rows = cursor.fetchall()
    headings = [i[0] for i in cursor.description]

    cursor.close()
    connection.close()

    return render_template(
        "teachers.html",
        rows=rows,
        headings=headings
    )


@app.route("/subjects")
def subjects():

    connection = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT", 3306))
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM subjects")

    rows = cursor.fetchall()
    headings = [i[0] for i in cursor.description]

    cursor.close()
    connection.close()

    return render_template(
        "subjects.html",
        rows=rows,
        headings=headings
    )


if __name__ == "__main__":
    app.run(debug=True)
