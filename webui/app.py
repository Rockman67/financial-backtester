from flask import Flask, jsonify, render_template
import pathlib

# ---------- init ----------
app = Flask(__name__, static_folder="static")

# ---------- routes ----------
@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/results")
def results():
    result_dir = pathlib.Path(app.static_folder) / "results"
    files = sorted(f.name for f in result_dir.glob("*"))
    return render_template("results.html", files=files)

# ---------- entry-point ----------
if __name__ == "__main__":
    # слушаем ВСЕ интерфейсы и именно порт 8000,
    # он проброшен наружу в docker-compose.yml
    app.run(host="0.0.0.0", port=8000, debug=False)
