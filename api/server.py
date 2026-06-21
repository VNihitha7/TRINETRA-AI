from flask import Flask
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route("/stats")
def stats():

    conn = sqlite3.connect("violations.db")

    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM violations")
    total_cases = cur.fetchone()[0]

    cur.execute("SELECT MAX(severity) FROM violations")
    max_severity = cur.fetchone()[0]

    conn.close()

    data = {

        "helmet":18,

        "parking":9,

        "severity":max_severity,

        "cases":total_cases

    }

    return data


if __name__ == "__main__":

    app.run(debug=True)