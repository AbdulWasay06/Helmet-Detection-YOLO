from ultralytics import YOLO

# Load your trained weights
model = YOLO('weights/best.pt')

# Print the dictionary of class names
print("-" * 30)
print("YOUR MODEL CLASSES:")
print(model.names)
print("-" * 30)