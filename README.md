# Smart Object Detection with YOLO: Ask AI to Identify Phones, book, and People in Your Images

This Streamlit app allows you to upload an image and ask it to identify specific objects (phone, person, book) using a pre-trained YOLOv5 model. The app processes the image, runs object detection, and highlights detected objects by drawing bounding boxes. You can query the app by asking if a specific object (e.g., "Is there a phone?") is present in the image.

Features:
- Upload an image (JPEG, PNG, or JPG).
- Detects specific objects: phone, pen, glasses, and person.
- Ask the app: Query whether a particular object is in the image (e.g., "Is there a phone?").
- Visual feedback: Displays the image with bounding boxes drawn around detected objects.

How It Works:
- Uploads an image using Streamlit
- Runs YOLOv5 to detect objects in the image
- Filters detections to only include phone, pen, glasses, person
- Draws bounding boxes around detected objects

Allows the user to query whether a specific object is present in the image

Example Queries You Can Ask
- "Is there a phone?"
- "Do you see a pen?"
- "Is there a person in the image?"

Notes
This app uses YOLOv5s, a lightweight model trained on COCO dataset.
You can extend this by adding more objects, changing model weights, or improving UI.
The app is optimized for simplicity, making it fast and easy to use.

Libraries Used:
- Streamlit: For building the web app.
- YOLOv5: For object detection (using the ultralytics package).
- OpenCV and Pillow: For image manipulation. CV2
- NumPy
- Torch

Cloning the Repository
To use the YOLO Object Detection app locally, follow these steps:

1. Clone the Repository
git clone https://github.com/ErikElcsics/Build-Smart-object-detection-YOLO-ask-AI-to-identify-phones-people-book-in-your-images.git
cd yolo-object-detection-app

Installation Instructions
Follow these steps to set up the project and run the app on your local machine.

2. Set Up a Virtual Environment (optional but recommended)
It is highly recommended to set up a virtual environment to manage your dependencies. You can use venv (Python's built-in virtual environment tool), PyCharm, or Conda.

For venv:

python -m venv venv
Activate the virtual environment:

Windows:
.\venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

3. Install Dependencies
Install the necessary packages directly using:
pip install streamlit torch torchvision opencv-python pillow ultralytics

4. Run the App
Once the dependencies are installed, you can run the Streamlit app using the following command:
streamlit run Smart_Yolo_Object_Detector.py
This will start the app and open it in your default web browser.

How to Use the App
- Upload an image: Choose a .jpg, .jpeg, or .png image that you want to test. The app will automatically detect objects from the allowed list (phone, pen, glasses, and person) and display bounding boxes around detected objects.
- Ask a question: Use the text input box to ask if a specific object (e.g., "Is there a phone?") is present in the image.
	- "Is there a phone?"
	- "Do you see a pen?"
	- "Are there any glasses?"
	- "Is there a person in the image?" 
        - Also, ask for objects that you know are not in the picture

The app will respond with either a confirmation or a warning based on the detection.

License
This project is licensed under the MIT License - see the LICENSE file for details.

![image](https://github.com/user-attachments/assets/c9b0d585-160d-4d6d-9017-bf442d7b7f86)

![image](https://github.com/user-attachments/assets/88ab920c-04e1-40a5-9c0d-71ecdbf3f2a8)

![image](https://github.com/user-attachments/assets/e19872ac-4822-4985-9550-1b6f841a1e4f)



