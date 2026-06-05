import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8s.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    # Detect objects
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Show result
    cv2.imshow("Real-Time Object Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()