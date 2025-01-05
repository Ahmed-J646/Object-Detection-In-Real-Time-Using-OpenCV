Gun Detection App project:


# Gun Detection App

This is a **Gun Detection App** built using **Streamlit** and **OpenCV**. The app detects guns in uploaded images using a pre-trained Haar Cascade classifier and displays the results, highlighting detected guns with bounding boxes.

## Features
- Upload an image file (JPEG, PNG).
- Detect guns in the image using OpenCV's Haar Cascade.
- Display the processed image with bounding boxes around detected guns.
- Save the processed image with a timestamped filename.
- Display messages about detection results.

## Prerequisites
- Python 3.7 or later.
- `cascade.xml` Haar Cascade file for gun detection (must be in the same directory as the script).

## Installation

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/Ahmed-J646/Object-Detection-In-Real-Time-Using-OpenCV.git
   cd gun-detection-app
Install the required dependencies:


pip install streamlit opencv-python numpy pillow
Ensure you have the cascade.xml file in the same directory as the app script.

Usage
Run the Streamlit app:


streamlit run app.py
Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

Upload an image and view the results.

The processed image is saved in the project directory with a timestamped filename.

Directory Structure
.
├── app.py              # Main application script
├── cascade.xml         # Haar Cascade file for gun detection
├── README.md           # Documentation
├── requirements.txt    # List of dependencies
Example Output
No guns detected: The app displays a success message: No guns detected in the image.

Guns detected: The app displays a warning message and highlights detected guns with bounding boxes in the image.

Screenshots
Upload Interface:

Detection Results:

Notes
The Haar Cascade file (cascade.xml) is crucial for detection and must be trained for specific gun types.
The detection may not work optimally for complex backgrounds or low-resolution images.
Contributing
Feel free to fork the repository and submit a pull request with improvements or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenCV for image processing.
Streamlit for creating the interactive web app.
Pre-trained Haar Cascade file for gun detection.
