from ultralytics import YOLO

# 1. Load your model
model = YOLO('weights/best.pt')

# 2. Run detection on your video file
# save=True creates a video in runs/detect/predict/
# Use the folder name / file name
results = model.predict(source='traffic.mp4/test2.mp4', save=True, conf=0.5)

print("Video processing done! Check the 'runs/detect/predict' folder.")