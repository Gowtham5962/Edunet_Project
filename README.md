# Image Steganography Project

## Introduction
This project demonstrates the use of **steganography** for securely hiding text messages within images using **OpenCV**. The encrypted image maintains visual integrity while embedding the message, ensuring covert communication. A passcode is required for decryption, adding an extra layer of security.

## Features
- **Message Encryption:** Hides a secret message inside an image.
- **Password Protection:** Ensures only authorized users can decrypt the message.
- **Lossless Data Encoding:** Uses PNG format to preserve image quality.
- **Cross-Format Compatibility:** Supports encoding and decoding in multiple image formats (JPG and PNG).
- **User-Friendly Interface:** Simple command-line interaction for encoding and decoding.

## Technologies Used
- **Python**: Primary programming language.
- **OpenCV**: For image processing.
- **Hashlib**: For SHA-256 password hashing.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- OpenCV library (`pip install opencv-python`)

### Steps
1. Clone the repository or download the source code.
2. Install dependencies using:
   ```bash
   pip install opencv-python
   ```
3. Run the encryption script:
   ```bash
   python encryption.py
   ```
4. Run the decryption script:
   ```bash
   python decryption.py
   ```

## Usage
### Encryption Process
1. Run `encryption.py`.
2. Enter the secret message.
3. Provide a passcode.
4. The encrypted image will be saved and opened automatically.

### Decryption Process
1. Run `decryption.py`.
2. Enter the passcode used during encryption.
3. If correct, the hidden message will be revealed.

## End Users
- **Cybersecurity Professionals**: Securely transmit sensitive data.
- **Journalists & Whistleblowers**: Hide confidential information.
- **Students & Researchers**: Learn about steganography techniques.
- **Corporate & Government Agencies**: Protect classified information.

## Limitations
- Works best with **lossless formats (PNG)** as **JPG compression** may alter data.
- Message length is limited by the image size.
- Passcode security depends on user-provided strength.

## Conclusion
This project presents a **lightweight yet effective** method for securing text within images using **steganography and password protection**. It serves as a valuable tool for **secure communication and data privacy**, demonstrating practical applications in **cybersecurity and digital forensics**.

