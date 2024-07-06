import cv2

# Initialize video capture object with webcam index (usually 0)
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error opening webcam")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is captured successfully
    if not ret:
        print("Error capturing frame")
        break

    # Display the resulting frame (optional for demo purposes)
    cv2.imshow('Webcam Feed', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture object and close all windows
cap.release()
cv2.destroyAllWindows()

print("Webcam access terminated.")
