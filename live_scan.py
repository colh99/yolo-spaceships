'''
Opens a window and checks the screen (live!) for a specific object using the YOLO model. 
Uses the ready_models/best.pt model for the weights.
'''

import cv2
import numpy as np
from mss import mss
from ultralytics import YOLO

# Load the YOLO model (replace 'yolov8n.pt' with your custom-trained model if needed)
model = YOLO('ready_models/best.pt')

# Define the screen capture region (adjust as needed)
monitor = {"top": 440, "left": 1000, "width": 640, "height": 640} # center ish of a 1440p screen

# Initialize screen capture
sct = mss()

# Create a named window and set it to always be on top
window_name = "YOLO Live Screen Detection"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

print("Press 'q' to quit.")

while True:
    # Capture the screen
    screenshot = sct.grab(monitor)
    frame = np.array(screenshot)

    # Convert the frame to BGR (OpenCV uses BGR format)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    # Run YOLO detection
    results = model.predict(source=frame, save=False, conf=0.2, show=False)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow(window_name, annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()