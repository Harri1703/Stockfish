import pypyodbc as odbc
from flask import Flask, request, jsonify

connection_string = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:stockfish-server.database.windows.net,1433;Database=MPEDA;Uid=stockfish;Pwd=GTAv@1703;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

conn = odbc.connect(connection_string)

cursor = conn.cursor()

app = Flask(__name__)


@app.route("/new-contact", methods=["POST"])
def new_contact():
    data = request.get_json()
    cursor.execute(
        f"INSERT INTO contact_details (firstname,lastname,mobilenumber,email) VALUES ('{data['firstname']}','{data['lastname']}','{data['mobilenumber']}','{data['email']}')"
    )
    conn.commit()

    file_path = "transcript.txt"

    text_to_write = (
        "MPEDA Assistant : Hi, I am your MPEDA AI Assistant, How can I help you ?"
    )

    with open(file_path, "w") as file:
        file.write(text_to_write + "\n")

    return jsonify({"status": "success"}), 201


if __name__ == "__main__":
    app.run(debug=True, port=7001)
