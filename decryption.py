import cv2
import os

def decrypt_image():
    # Hardcoded encrypted image path
    img_path = r"C:\Users\gowth\Edunet\encryptedImage.png"
    print(f"Loading image from: {os.path.abspath(img_path)}")
    img = cv2.imread(img_path)
    
    if img is None:
        print("Error: Image not found or unable to load.")
        return
    
    # Extract data from the image
    data = ""
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                # Extract the character from the pixel value
                char = chr(img[i, j, k])
                data += char
    
    # Extract password and message
    pas = input("Enter passcode for Decryption: ")
    password = data[:len(pas)]
    message = data[len(pas):data.find('\0')]
    
    print(f"Extracted password: {password}")
    print(f"Entered passcode: {pas}")
    
    # Verify the password
    if password == pas:
        print("Decoded message:", message)
    else:
        print("YOU ARE NOT auth")

if __name__ == "__main__":
    decrypt_image()
