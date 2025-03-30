import streamlit as st
import torch
import numpy as np
import cv2
from PIL import Image
from ultralytics import YOLO

# Load the YOLO model (pre-trained on COCO dataset)
model = YOLO("yolov5s.pt")  # Using YOLOv5 small model

# Allowed object names (COCO dataset names mapped to our custom labels)
ALLOWED_CLASSES = {"cell phone": "phone", "person": "person", "book": "book"}

# Streamlit UI
st.title("Smart Object Detection YOLO App: Ask AI to Identify Phones, Book and People in Your Images")
st.write("Upload an image and ask if it contains certain objects (phone, person, book).")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Convert file to an OpenCV image
    image = Image.open(uploaded_file)
    image = np.array(image)

    # Convert RGB to BGR for OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Run YOLO object detection
    results = model(image)  # Returns a list of results

    detected_objects = []

    # Extract detections from the first result
    for result in results:  # Iterate through YOLO results
        for box in result.boxes:  # Get bounding boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordinates
            conf = box.conf[0].item()  # Confidence score
            cls_id = int(box.cls[0].item())  # Class ID
            cls_name = model.names[cls_id]  # Get class name

            # Check if the detected class is in our allowed list
            if cls_name in ALLOWED_CLASSES:
                detected_objects.append(ALLOWED_CLASSES[cls_name])

                # Draw a rectangle around detected object
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, f"{ALLOWED_CLASSES[cls_name]} ({conf:.2f})",
                            (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Convert BGR to RGB for Streamlit display
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Show processed image with detections
    st.image(image, caption="Detected Objects", use_container_width=True)

    # Ask the user for a specific object
    st.write("Ask if there a phone?")
    st.write("Ask is there a person in the image?")
    st.write("Ask if do you see a book?")

    object_query = st.text_input("Ask if an object is in the image (e.g., 'Is there a phone?')").strip().lower()

    if object_query:
        found = any(obj in object_query for obj in detected_objects)
        if found:
            st.success("✅ Yes, the object is present in the image!")
        else:
            st.warning("❌ No, the object was not detected.")
