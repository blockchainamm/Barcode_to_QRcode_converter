# Import required libraries
import sys
import cv2
from pyzbar.pyzbar import decode
import qrcode # Import qrcode package
import os
  
# Function to decode barcode from a given image
def barcodeReader(image):
     
    # read the image in numpy array using cv2
    img = cv2.imread(image)
      
    # Decode the barcode image
    detectedBarcodes = decode(img)
      
    # If not detected then print the message
    if not detectedBarcodes:
        print(f"Barcode cannot be decoded from the image {image} or your barcode is blank/ indecipherable!")
        barcode_data = 'none'
    else:
       
        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes: 
           
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
             
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)
             
            if barcode.data!="":
               
            # Print the barcode data
                print(barcode.data)
                print(barcode.type)
                barcode_data = barcode.data
    
                     
    # Display the image
    cv2.imshow("Image", img)
    # cv2.waitkey() method waits till we exit or click on the close button
    cv2.waitKey(0)

    return barcode_data 
    # call the sys.exit() method to safely exit the technique
    sys.exit() # to exit from all the processes

# Function to generate QR code from decoding of bar code
def QRcode_gen(barcode_data):
    qr = qrcode.QRCode(version=10,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=20,
                    border=3)

    qr.add_data(barcode_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="darkblue", back_color="white")
    img.save("qrcode.png")    

# Function to check if file exists in the current working directory
def check_file(imagefile):
    # Get current working directory
    current_dir = os.getcwd()
    # Join current directory with file name
    path = os.path.join(current_dir, imagefile)

    # Check whether the specified
    # path exists or not
    isExist = os.path.exists(path)
    #print(isExist)
    return isExist

if __name__ == "__main__":
  # Take the image file from user and assign it to a variable image
    imagefile = input("Enter file with bardcode image: ")
    print(f"The file name which you entered is: {imagefile}" )
    
    # Check if the file exists in the current directory
    existcheck = check_file(imagefile)
    
    # If the image file exists then decode image
    if existcheck:
        barcodedata = barcodeReader(imagefile)
    
        # Check barcode data to generate QR code
        if barcodedata != 'none':
            QRcode_gen(barcodedata)
        else:
            print('QR code cannot be generated for barcode blank/ indecipherable!') 
    else:
        print(f'No such file {imagefile} found in this directory')           

# Destroy all the created windows using cv2.destroyAllWindows()
cv2.destroyAllWindows()
