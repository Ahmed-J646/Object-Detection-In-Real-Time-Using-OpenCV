import streamlit as st
import cv2
import numpy as np
from PIL import Image
import datetime

# Load the cascade classifier:
gun_cascade = cv2.CascadeClassifier('cascade.xml')  # Ensure you have this file in the same folder

# Function to detect guns in the image
def detect_guns(image):
    gun_exist = False
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    guns = gun_cascade.detectMultiScale(gray, 1.3, 20, minSize=(100, 100))
    for (x, y, w, h) in guns:
        gun_exist = True
        # Draw bounding box around detected guns
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return image, gun_exist

# Streamlit app
st.title("Gun Detection App")
st.write("Upload an image, and the app will detect guns in it using OpenCV!")

# Image uploader
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded image to OpenCV format:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Perform gun detection
    processed_image, gun_exist = detect_guns(image)

    # Display results
    st.image(processed_image, channels="BGR", caption="Processed Image")
    if gun_exist:
        st.warning("Gun detected in the image!")
    else:
        st.success("No guns detected in the image.")

    # Save the processed image with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"processed_{timestamp}.jpg"
    cv2.imwrite(output_filename, processed_image)
    st.write(f"Processed image saved as: `{output_filename}`")

else:
    st.info("Please upload an image to start gun detection.")

    

