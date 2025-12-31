from ultralytics import YOLO
import os

def train_helmet_model():
    # 1. Load the YOLOv8 Nano model (the best for real-time projects)
    model = YOLO('yolov8n.pt')

    # 2. Get the absolute path to our data.yaml
    # This avoids "File Not Found" errors on Windows
    dataset_path = os.path.join(os.getcwd(), 'datasets', 'data.yaml')

    # 3. Start training
    # We use 25 epochs so you can see results today
    model.train(
        data=dataset_path, 
        epochs=25, 
        imgsz=640, 
        batch=16, 
        name='helmet_training_run'
    )

if __name__ == '__main__':
    train_helmet_model()