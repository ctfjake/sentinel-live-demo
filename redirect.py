from flask import Blueprint, request, redirect

bp = Blueprint("redirectbp", __name__)


@bp.route("/go")
def go():
    # VULN: open redirect - user-controlled destination, no allowlist
    target = request.args.get("url")
    return redirect(target)
