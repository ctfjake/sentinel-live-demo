import os
from flask import Blueprint, request

bp = Blueprint("pingbp", __name__)


@bp.route("/ping")
def ping():
    # VULN: OS command injection - user host concatenated into shell command
    host = request.args.get("host", "localhost")
    return os.popen("ping -c 1 " + host).read()
