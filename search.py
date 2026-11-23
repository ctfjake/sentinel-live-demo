from flask import Blueprint, request

bp = Blueprint("searchbp", __name__)


@bp.route("/search")
def search():
    # VULN: reflected XSS - user input echoed into HTML without escaping
    q = request.args.get("q", "")
    html = "<html><body>Results for: " + q + "</body></html>"
    return html
