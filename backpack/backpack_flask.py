from flask import Flask,g
import sqlite3


app = Flask(__name__)
DATABASE = 'backpack/backpack.db'

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g.database = sqlite3.connect(DATABASE)
    return db
#get database

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
#close connection

@app.route("/")
def index():
    cursor = get_db().cursor()
    sql = "SELECT * FROM contents"
    cursor.execute(sql)
    results = cursor.fetchall()
    return str(results)

if __name__ == "__main__":
    app.run(debug=True)