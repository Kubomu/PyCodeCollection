"""
Generate a QR code from user input data.

Example:
    >>> python qrcode_generator.py
    Enter the data you want to encode: https://github.com/Kubomu
    # This will generate a QR code image file named 'qr_code.png' in the current directory

Parameters:
    data (str): The data to be encoded in the QR code

Returns:
    None

"""
import qrcode
from PIL import Image

def generate_qr_code():
    """
    Generate a QR code from user input data.
    """
    # The data you want to encode in the qr code
    data = input('Enter the data you want to encode: ')

    # Generate the qr code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the qr code
    image = qr.make_image(fill='black', back_color='white')

    # Save the image
    image.save('qr_code.png')
    Image.open('qr_code.png')

if __name__ == "__main__":
    generate_qr_code()