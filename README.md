# Flask Image-Based AES Encryption and Decryption

This project implements a Flask web application that provides a simple interface to encrypt and decrypt plaintext using AES (Advanced Encryption Standard) encryption, with an image serving as the encryption key. The key is generated based on the hash of the uploaded image. Users can upload an image along with their plaintext to encrypt, and then use the same image to decrypt the ciphertext.

## Features
AES Encryption and Decryption: Uses the AES algorithm in CBC mode for encryption and decryption.
Image-Based Key: Generates a key based on the SHA-256 hash of the uploaded image.
Flask Web Interface: Simple and user-friendly web interface for encrypting and decrypting text.
Error Handling: Handles invalid inputs and errors during the decryption process.

## PrerequisitesTo run this project, you need to have the following installed:

Python 3.x
Flask
PyCryptodome

## Installation
Clone this repository to your local machine.
bash
Copy code
git clone https://github.com/yourusername/flask-image-encryption.git
Navigate to the project directory.
bash
Copy code
cd flask-image-encryption
Create and activate a virtual environment (optional but recommended).
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required Python packages.
bash
Copy code
pip install -r requirements.txt
Running the App
Run the Flask development server.
bash
Copy code
python app.py
Open a web browser and navigate to http://127.0.0.1:5000/.

## How It Works
Encryption
The user uploads an image file and enters plaintext to encrypt.
The system computes the SHA-256 hash of the image and uses it as the AES encryption key.
The plaintext is encrypted using AES in CBC mode, and the resulting ciphertext is shown to the user.
Decryption
The user uploads the same image used for encryption and enters the ciphertext.
The system regenerates the AES key using the uploaded image and decrypts the ciphertext.
The original plaintext is displayed if decryption is successful.
Project Structure
php
Copy code
├── app.py                   # Main Flask application
├── templates/                # HTML templates for Flask views
│   ├── index.html            # Main page for encryption
│   ├── decrypt.html          # Page for decryption
├── static/                   # Directory for temporary storage of uploaded images
├── requirements.txt          # List of Python dependencies
├── README.md                 # Project documentation

## Dependencies
Flask: For building the web application.
PyCryptodome: For cryptographic functions like AES encryption, decryption, and SHA-256 hashing.
To install dependencies, simply run:

bash
Copy code
pip install -r requirements.txt
Usage
Encryption: Upload an image and enter plaintext, then click the encrypt button. The application will return the ciphertext.
Decryption: Upload the same image and enter the ciphertext to decrypt and retrieve the original text.

## Example
Encryption
Input Image: my_image.jpg
Input Text: Hello, world!
Output Ciphertext: 6f84ad23d4f... (hexadecimal format)
Decryption
Input Image: my_image.jpg
Input Ciphertext: 6f84ad23d4f...
Output Plaintext: Hello, world!

## Error Handling
If an incorrect image or invalid ciphertext is provided during decryption, an error message will be shown: Decryption unsuccessful. Invalid ciphertext or key.