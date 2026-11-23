from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return "Sentinel live demo app. See /hello."


@app.route("/hello")
def hello():
    # Safe baseline: name is escaped by Jinja autoescaping
    name = request.args.get("name", "world")
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)


if __name__ == "__main__":
    app.run(debug=False, port=5000)
