# Car Detection Web Application

This project is a web-based application that allows users to interact with a YOLOv5 machine learning model for object detection. Users can upload images for model comparison or stream a YouTube video for real-time detection. The application demonstrates the effectiveness of YOLOv5 and a custom-trained model using COCO dataset filters for detecting cars.

---

## Features

- **Image Comparison**: Upload an image and view side-by-side detection results between:
  - `yolov5s.pt` (pre-trained YOLOv5 model).
  - A custom model trained for detecting cars.
---

## Why YOLOv5?

YOLOv5s was chosen as the object detection model for this project because of the following reasons:

1. **Speed and Efficiency**:
   - YOLOv5s is the smallest and fastest variant of YOLOv5, making it ideal for real-time applications requiring low latency.
   - It balances computational cost with competitive accuracy, making it an efficient choice.

2. **Ease of Use**:
   - YOLOv5 has an intuitive interface and well-documented API, with pre-trained weights readily available.
   - It supports transfer learning, making it easy to fine-tune for custom datasets.

3. **Versatility**:
   - Supports various input types (images, videos, streams) and runs seamlessly on CPUs, GPUs, and cloud environments.

4. **Community Support**:
   - YOLOv5 is widely adopted, ensuring strong community support and abundant resources for troubleshooting and enhancement.

5. **Real-Time Compatibility**:
   - Its architecture is optimized for tasks requiring real-time detection, such as video streaming.

---

## Why the COCO Dataset?

The COCO dataset was chosen to fine-tune the custom model because of the following reasons:

1. **Comprehensive Coverage**:
   - COCO contains diverse object categories, including a well-represented "car" class, making it suitable for detecting vehicles in various scenarios.

2. **Pre-Trained Models**:
   - YOLOv5 models are pre-trained on COCO, providing a strong baseline for transfer learning.

3. **Data Quality**:
   - COCO annotations are high-quality, with diverse images that include cars in urban environments, highways, and other real-world settings.

4. **Ease of Transfer Learning**:
   - Filtering COCO for the "car" category enables rapid adaptation to tasks focusing on vehicle detection.

---

## Limitations

1. **Model Accuracy**:
   - While YOLOv5s is fast, it may lack accuracy when detecting small or overlapping objects compared to heavier models (e.g., YOLOv5m, YOLOv5l).

2. **Real-Time Detection**:
   - I did not have time to setup the real-time video objectdetection.
   - Real-time processing depends on the user's hardware; older CPUs or GPUs may cause delays.

4. **Video Streaming**:
   - Streaming from YouTube requires a stable internet connection for smooth operation.

---

## Setup Instructions

### Prerequisites

1. **Python**: Install Python 3.8 or higher.
2. **Git**: Ensure Git is installed on your system.
3. **Environment**: Use a virtual environment to avoid dependency conflicts.

---

### Steps to Run the Application

1. **Clone This Repository**:
   ```bash
   git clone https://github.com/Francisco0561/web-app-object-detection.git
   cd web-app-object-detection
2. **Install Dependencies**:
   ```bash
   pip install flask flask-cors torch torchvision matplotlib 
   pip install -r yolov5/requirements.txt
3. **Clone the YOLOv5 repository**:
   ```bash
   git clone https://github.com/ultralytics/yolov5.git
5. **Download Pre-Trained Weights**:
   - Download yolov5s.pt from the YOLOv5 release page
   - Place it in the yolov5 directory
   - Then do the same for your own model or another model
6. Run the Application:
   ```bash
   python.py
7. Access the Web App:
   - Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
  
---

## Techonology Stack
**Backend:** Flask
**Frontend:** HTML, Tailwind CSS
**Model:** YOLOv5s and custom-trained YOLOv5

   
