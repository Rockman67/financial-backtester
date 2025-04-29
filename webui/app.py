from flask import Flask, jsonify, render_template
import pathlib

app = Flask(__name__, static_folder="static")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/results")
def results():
    result_dir = pathlib.Path(app.static_folder) / "results"
    result_dir.mkdir(exist_ok=True, parents=True)
    files = sorted(f.name for f in result_dir.glob("*"))
    return render_template("results.html", files=files)
