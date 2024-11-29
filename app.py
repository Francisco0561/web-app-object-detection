from flask import Flask, render_template, request, jsonify, send_file
import os
from pathlib import Path
from yolov5 import detect

app = Flask(__name__)
UPLOAD_FOLDER = Path('uploads/')
OUTPUT_FOLDER = Path('outputs/')
MODEL1_PATH = Path('yolov5/yolov5s.pt')  # Pretrained model
MODEL2_PATH = Path('yolov5/best.pt')  # Custom model

# Ensure upload and output folders exist
UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

@app.route('/')
def index():
    """Render the main HTML page."""
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_objects():
    """Handle object detection requests with two models."""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    # Save the uploaded file
    file = request.files['file']
    input_path = UPLOAD_FOLDER / file.filename
    file.save(input_path)

    try:
        # Perform detection with Model 1
        detect.run(
            weights=str(MODEL1_PATH),
            source=str(input_path),
            imgsz=(640, 640),
            conf_thres=0.25,
            iou_thres=0.45,
            max_det=1000,
            device="cpu",
            nosave=False,
            project=str(OUTPUT_FOLDER),
            name="model1",
            exist_ok=True
        )

        # Perform detection with Model 2
        detect.run(
            weights=str(MODEL2_PATH),
            source=str(input_path),
            imgsz=(640, 640),
            conf_thres=0.25,
            iou_thres=0.45,
            max_det=1000,
            device="cpu",
            nosave=False,
            project=str(OUTPUT_FOLDER),
            name="model2",
            exist_ok=True
        )

        # Correct file paths
        output1_path = OUTPUT_FOLDER / "model1" / file.filename
        output2_path = OUTPUT_FOLDER / "model2" / file.filename

        # Validate file existence
        if not output1_path.exists():
            print(f"File not found: {output1_path}")
            return jsonify({"error": f"Model 1 result not found for {file.filename}"}), 404

        if not output2_path.exists():
            print(f"File not found: {output2_path}")
            return jsonify({"error": f"Model 2 result not found for {file.filename}"}), 404

        # Return URLs for both results
        return jsonify({
            "model1_image": f"/outputs/model1/{file.filename}",
            "model2_image": f"/outputs/model2/{file.filename}"
        })

    except Exception as e:
        print(f"Error during detection: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/outputs/<subdir>/<filename>')
def serve_output_image(subdir, filename):
    """Serve the detected image for display."""
    output_path = OUTPUT_FOLDER / subdir / filename

    if not output_path.exists():
        print(f"File not found: {output_path}")
        return jsonify({"error": f"File {filename} not found in {subdir}"}), 404

    return send_file(output_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
