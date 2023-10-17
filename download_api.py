from flask import Flask, send_file

app = Flask(__name__)


@app.route("/get-file", methods=["GET"])
def download_text_file():
    file_path = "transcript.txt"

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=7003)
