import cv2
from ultralytics import YOLO

# Load ONLY your custom model
model = YOLO('weights/best.pt')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # Set confidence to ALMOST ZERO (0.01) to see any guess the AI has
    results = model(frame, conf=0.01)
    
    for r in results:
        for box in r.boxes:
            conf = float(box.conf)
            print(f"AI is {conf*100:.1f}% sure there is a helmet here.")

    annotated_frame = results[0].plot()
    cv2.imshow("Extreme Sensitivity Test", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()