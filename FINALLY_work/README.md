# Image Processing Web Application

Welcome to our Image Processing Web Application! This single-page application allows users to upload images, perform various image processing tasks, and save the modified images in their profiles.



## Technologies Used

- **Flask:** We used Flask, a lightweight web application framework in Python, to create the backbone of our web application.
- **Pillow:** Pillow is a Python Imaging Library that provides tools for modifying images, which we utilized for image processing.

## Features

- **User Authentication:** Users can register and log in to access their profiles.
- **Image Upload:** Users can upload images directly to the application.
- **Image Processing:** Users can perform various image processing tasks such as adjusting brightness, contrast, resizing, and rotating images.
- **Image Storage:** Processed images are saved in the user's profile for easy access and download.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependencies: pip install Flask Pillow Flask-MongoEngine
3. Set up MongoDB and configure your database settings in the Flask application:
   
4. Run the Flask application:
   python app.py
5. Open a web browser, go to http://localhost:5000/ to see the homepage of the image processing web application.