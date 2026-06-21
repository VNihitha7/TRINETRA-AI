from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/violations")
def violations():

    conn = sqlite3.connect("violations.db")

    cur = conn.cursor()

    cur.execute("""

    SELECT plate,
           severity,
           confidence,
           timestamp

    FROM violations

    ORDER BY id DESC

    LIMIT 10

    """)

    rows = cur.fetchall()

    conn.close()

    data = []

    for row in rows:

        data.append({

            "plate": row[0],
            "severity": row[1],
            "confidence": row[2],
            "timestamp": row[3]

        })

    return jsonify(data)


if __name__ == "__main__":

    app.run(debug=True)