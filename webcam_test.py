import cv2
from ultralytics import YOLO

# 1. Load models
my_model = YOLO('weights/best.pt')
base_model = YOLO('yolov8n.pt') 

cap = cv2.VideoCapture(0)

# Settings to fix the flickering
CONF_THRESHOLD = 0.20 # Lower this to 0.15 if it still misses the helmet
SMOOTHING_FRAMES = 5  # It must miss the helmet for 5 frames to turn Red
helmet_memory = 0      # Counter to track helmet presence

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    # A. Detect Person & Helmet
    person_results = base_model(frame, classes=0, conf=0.5, verbose=False)
    helmet_results = my_model(frame, conf=CONF_THRESHOLD, verbose=False)

    p_boxes = person_results[0].boxes.xyxy.cpu().numpy() if person_results[0].boxes else []
    h_boxes = helmet_results[0].boxes.xyxy.cpu().numpy() if helmet_results[0].boxes else []

    # B. Check if any helmet is detected in the whole frame
    if len(h_boxes) > 0:
        helmet_memory = SMOOTHING_FRAMES # Reset memory counter
    elif helmet_memory > 0:
        helmet_memory -= 1 # Countdown if helmet is missing

    # C. Determine Safety State
    is_safe = (helmet_memory > 0)

    # D. Draw the Person Box
    for pb in p_boxes:
        px1, py1, px2, py2 = pb
        
        color = (0, 255, 0) if is_safe else (0, 0, 255)
        label = "Safe: Helmet" if is_safe else "VIOLATION: NO HELMET"
        
        # Draw main box
        cv2.rectangle(frame, (int(px1), int(py1)), (int(px2), int(py2)), color, 3)
        
        # Draw background for text (makes it look professional)
        cv2.rectangle(frame, (int(px1), int(py1) - 35), (int(px1) + 250, int(py1)), color, -1)
        cv2.putText(frame, label, (int(px1) + 5, int(py1) - 10), 
                    cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Safety Audit - Stable Mode", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
# python webcam_test.py