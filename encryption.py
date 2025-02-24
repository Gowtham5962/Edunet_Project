import cv2
import os

def encrypt_image(msg, password):
    # Hardcoded image path
    img_path = r"C:\Users\gowth\Edunet\encodedimage.jpg"
    print(f"Loading image from: {os.path.abspath(img_path)}")
    img = cv2.imread(img_path)
    
    if img is None:
        print("Error: Image not found or unable to load.")
        return
    
    # Add a null character to mark the end of the message
    msg += '\0'
    
    # Combine password and message
    data = password + msg
    
    # Embed data into the image
    index = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                if index < len(data):
                    # Embed the character into the pixel value
                    img[i, j, k] = ord(data[index])
                    index += 1
                else:
                    break
    
    # Save the encrypted image in PNG format (lossless)
    encrypted_image_path = r"C:\Users\gowth\Edunet\encryptedImage.png"
    cv2.imwrite(encrypted_image_path, img)
    print(f"Message has been encoded into '{os.path.abspath(encrypted_image_path)}'.")
    os.system(f"start {encrypted_image_path}")  # Open the image on Windows

if __name__ == "__main__":
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    encrypt_image(msg, password)
