# Missing Person Finder — MVP

A minimal working prototype: relief camps log photos, families search by uploading a photo, and the app returns AI-matched candidates using face recognition.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

> **Note on `face_recognition` install:** it depends on `dlib`, which needs a C++ compiler.
> - **Windows:** install "Desktop development with C++" via Visual Studio Build Tools first, or use `conda install -c conda-forge dlib` before `pip install face_recognition`.
> - **Mac:** `brew install cmake` first.
> - **Linux:** `sudo apt install cmake build-essential` first.

## Run

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

1. Go to **Log Camp Photo** and add a couple of test people (use your own consented photos).
2. Go to **Search for Someone** and upload a photo of one of them (or a different photo of the same person) to see the match.

## How matching works

Each photo is converted into a 128-number "face encoding" by `face_recognition`. Two photos are considered a match if the distance between their encodings is below `MATCH_THRESHOLD` (default `0.6`) in `app.py` — lower the number for stricter matching.

## Next steps

- Swap SQLite for PostgreSQL + real file storage (S3) for production use
- Add authentication so only verified camp staff can log photos
- Add a coordinator review step before any match is shown to a family
- See the main project README for the full roadmap and ethical considerations
