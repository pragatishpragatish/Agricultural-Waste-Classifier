# Agricultural Waste Management - Flask App

This project is a Flask-based web application that detects and classifies agricultural waste from images using YOLOv8. 
It then provides optimized recycling or reuse suggestions using Ollama's LLM.

## Features
✅ Upload images of agricultural waste  
✅ Detect waste types using YOLOv8  
✅ Retrieve recycling & reuse suggestions using LLM (Llama3.2)  
✅ Chat with the LLM for more details about recycling  
✅ Modern, responsive UI  

## Installation

1. **Clone the repository:**  
   ```sh
   git clone https://github.com/pragatishpragatish/Agricultural-Waste-Classifier.git
   cd Agricultural-Waste-Classifier
   ```

2. **Create a virtual environment (optional but recommended):**  
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Download & place the YOLOv8 model:**  
   - Ensure you have `yolov8_best_model.pt` in the project folder.

## Usage

1. **Run the Flask app:**  
   ```sh
   python app.py
   ```

2. **Access the web app:**  
   Open `http://127.0.0.1:5000/` in your browser.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET/POST | Upload an image for waste detection |
| `/ask` | POST | Ask LLM about waste recycling |

## Folder Structure
```
/agri-waste-flask
│-- /uploads          # Uploaded images storage
│-- /static           # Static files (CSS, JS)
│-- /templates        # HTML templates
│-- app.py            # Flask application
│-- requirements.txt  # Required dependencies
│-- README.md         # Project documentation
```

## Dependencies
- Flask  
- OpenCV  
- PyTorch  
- Ultralytics YOLOv8  
- Ollama  

## License
This project is licensed under the MIT License.
