from flask import Flask, render_template, request, redirect, url_for, flash
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For flashing messages

# Encryption and decryption functions here
def pad(data):
    padding_length = AES.block_size - (len(data) % AES.block_size)
    return data + bytes([padding_length] * padding_length)

def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt(key, plaintext):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = iv + cipher.encrypt(pad(plaintext))
    return ciphertext

def decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]))
    return plaintext

def get_image_key(image_path):
    with open(image_path, 'rb') as img_file:
        img_data = img_file.read()
        hash_obj = SHA256.new(img_data)
        return hash_obj.digest()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    if request.method == 'POST':
        image_file = request.files['image']
        plaintext = request.form['plaintext'].encode()

        # Ensure the static directory exists
        if not os.path.exists('static'):
            os.makedirs('static')

        # Save image temporarily to generate key
        image_path = os.path.join('static', image_file.filename)
        image_file.save(image_path)

        # Generate key and encrypt
        key = get_image_key(image_path)
        ciphertext = encrypt(key, plaintext)

        # Clean up temporary image
        os.remove(image_path)

        flash(f'Encryption successful! Ciphertext: {ciphertext.hex()}', 'success')
        return redirect(url_for('index'))


@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt_route():
    if request.method == 'POST':
        image_file = request.files['image']
        ciphertext_hex = request.form['ciphertext']

        # Save image temporarily to generate key
        image_path = os.path.join('static', image_file.filename)
        image_file.save(image_path)

        # Generate key
        key = get_image_key(image_path)

        try:
            # Attempt to decrypt
            ciphertext = bytes.fromhex(ciphertext_hex)  # Convert hex to bytes
            decrypted_text = decrypt(key, ciphertext).decode()

            # Check if the decrypted text is empty or invalid
            if not decrypted_text:
                raise ValueError("Decryption resulted in empty text.")

            # If successful, flash success message
            flash(f'Decryption successful! Decrypted text: {decrypted_text}', 'success')

        except (ValueError, KeyError, UnicodeDecodeError) as e:
            # Catch decryption errors and flash failure message
            flash('Decryption unsuccessful. Invalid ciphertext or key.', 'danger')

        # Clean up temporary image
        os.remove(image_path)

        return redirect(url_for('index'))

    return render_template('decrypt.html')


if __name__ == '__main__':
    app.run(debug=True)
