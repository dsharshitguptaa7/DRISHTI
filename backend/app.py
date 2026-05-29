from flask import Flask, request, jsonify
from detector import detect_objects, summarize_objects
import os
from speech import speak

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "DRISHTI API Running"


@app.route("/detect", methods=["GET", "POST"])
def detect():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)

    image.save(filepath)

    objects = detect_objects(filepath)

    summary = summarize_objects(objects)

    print(summary)

    # 🔊 Speech Text
    speech_text = ". ".join(summary)

    speak(speech_text)

    return jsonify({
        "detected_objects": objects,
        "summary": summary
    })


if __name__ == "__main__":
    app.run(debug=True)