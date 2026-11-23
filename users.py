import sqlite3
from flask import Blueprint, request

bp = Blueprint("usersbp", __name__)


@bp.route("/user")
def get_user():
    # VULN: SQL injection via string concatenation of user input
    uid = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE id = '" + uid + "'"
    cur.execute(query)
    rows = cur.fetchall()
    return str(rows)
