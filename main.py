from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path="/", static_folder="client/public")


@app.route("/")
def main():
    return send_from_directory("client/public", "index.html")


app.run(debug=True, port=5500)
