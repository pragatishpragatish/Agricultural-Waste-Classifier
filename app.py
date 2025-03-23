from flask import Flask, request, jsonify, render_template, send_from_directory
import ollama
import os
import cv2
import torch
from ultralytics import YOLO

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Load YOLO model
model = YOLO("yolov8_best_model.pt")  # Use your trained model

# Define waste class labels
CLASS_NAMES = {
    1: "Peels",
    2: "Potato Skin",
    3: "Egg Shell",
    4: "Sugarcane Husk",
    5: "Crop Straw"
}

def detect_waste(image_path):
    """Run YOLO detection and return detected waste classes."""
    results = model(image_path)
    detected_classes = set()

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls)
            detected_classes.add(CLASS_NAMES.get(cls_id, "Unknown"))

    return list(detected_classes)

def query_llama3(detected_classes):
    """Query Ollama (llama3.2:latest) with detected waste classes for recycling info."""
    prompt = f"How can the following waste materials be recycled or reused? {', '.join(detected_classes)}"
    response = ollama.chat(model="llama3.2:latest", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return jsonify({"error": "No file uploaded!"})

        file = request.files["image"]
        if file.filename == "":
            return jsonify({"error": "No file selected!"})

        # Save the uploaded file
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(image_path)

        # Run detection
        detected_classes = detect_waste(image_path)

        # Get recycling suggestions
        recycling_info = query_llama3(detected_classes)

        return render_template(
            "result.html",
            classes=detected_classes,
            recycling_info=recycling_info,
            uploaded_image_url=f"/uploads/{file.filename}"  # Pass correct image URL
        )

    return render_template("index.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    """Serve uploaded images so they can be displayed in the browser."""
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/ask", methods=["POST"])
def ask_llm():
    data = request.json
    question = data.get("question", "")
    
    response = ollama.chat(model="llama3.2:latest", messages=[{"role": "user", "content": question}])
    return jsonify({"answer": response["message"]["content"]})


if __name__ == "__main__":
    app.run(debug=True)
