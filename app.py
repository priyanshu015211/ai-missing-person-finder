import os
import sqlite3
import numpy as np
import face_recognition
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-me"

UPLOAD_FOLDER = "static/uploads"
DB_PATH = "camp_records.db"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
MATCH_THRESHOLD = 0.6  # lower = stricter match. 0.6 is face_recognition's default.

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS camp_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            camp_location TEXT NOT NULL,
            photo_path TEXT NOT NULL,
            encoding BLOB NOT NULL,
            date_logged TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def save_camp_record(name, camp_location, photo_path, encoding):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO camp_records (name, camp_location, photo_path, encoding) VALUES (?, ?, ?, ?)",
        (name, camp_location, photo_path, encoding.astype(np.float64).tobytes()),
    )
    conn.commit()
    conn.close()


def get_all_records():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT id, name, camp_location, photo_path, encoding, date_logged FROM camp_records"
    ).fetchall()
    conn.close()
    records = []
    for row in rows:
        records.append(
            {
                "id": row[0],
                "name": row[1],
                "camp_location": row[2],
                "photo_path": row[3],
                "encoding": np.frombuffer(row[4], dtype=np.float64),
                "date_logged": row[5],
            }
        )
    return records


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/camp/upload", methods=["GET", "POST"])
def camp_upload():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        camp_location = request.form.get("camp_location", "").strip()
        photo = request.files.get("photo")
        consent = request.form.get("consent")

        if not consent:
            flash("Consent is required before logging a photo.")
            return redirect(url_for("camp_upload"))

        if not name or not camp_location or not photo or not allowed_file(photo.filename):
            flash("Please fill all fields and upload a valid photo (png/jpg/jpeg).")
            return redirect(url_for("camp_upload"))

        filename = secure_filename(f"{name}_{photo.filename}")
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        photo.save(photo_path)

        image = face_recognition.load_image_file(photo_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            os.remove(photo_path)
            flash("No face detected in that photo. Please try a clearer image.")
            return redirect(url_for("camp_upload"))

        save_camp_record(name, camp_location, photo_path, encodings[0])
        flash(f"{name} has been logged at {camp_location}.")
        return redirect(url_for("camp_upload"))

    return render_template("camp_upload.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    matches = []
    if request.method == "POST":
        photo = request.files.get("photo")
        if not photo or not allowed_file(photo.filename):
            flash("Please upload a valid photo (png/jpg/jpeg).")
            return redirect(url_for("search"))

        filename = secure_filename(f"query_{photo.filename}")
        query_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        photo.save(query_path)

        image = face_recognition.load_image_file(query_path)
        encodings = face_recognition.face_encodings(image)

        if len(encodings) == 0:
            flash("No face detected in the uploaded photo. Please try another image.")
            return redirect(url_for("search"))

        query_encoding = encodings[0]
        records = get_all_records()

        for record in records:
            distance = np.linalg.norm(record["encoding"] - query_encoding)
            if distance < MATCH_THRESHOLD:
                confidence = round(max(0, (1 - distance)) * 100, 1)
                matches.append(
                    {
                        "name": record["name"],
                        "camp_location": record["camp_location"],
                        "photo_path": record["photo_path"],
                        "confidence": confidence,
                        "date_logged": record["date_logged"],
                    }
                )

        matches.sort(key=lambda m: m["confidence"], reverse=True)

    return render_template("results.html", matches=matches)


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)
