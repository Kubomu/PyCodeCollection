from captcha.image import ImageCaptcha
from PIL import Image 
import matplotlib.pyplot as plt

def generate_captcha_text(length):
    """
    Generates a random CAPTCHA text of the specified length.

    Args:
        length (int): The length of the CAPTCHA text.

    Returns:
        str: A random CAPTCHA text of the specified length.

    Example:
        >>> generate_captcha_text(7)
        'aBc123d'
    """
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_captcha(captcha_length=7, save_path='CAPTCHA.png'):
    """
    Generates a CAPTCHA image with the specified text length and saves it to the specified path.

    Args:
        captcha_length (int, optional): The length of the CAPTCHA text. Defaults to 7.
        save_path (str, optional): The path to save the CAPTCHA image. Defaults to 'CAPTCHA.png'.

    Returns:
        str: The CAPTCHA text.

    Example:
        >>> generate_captcha(7, 'my_captcha.png')
        'aBc123d'
    """
    image = ImageCaptcha(width=500, height=100)
    captcha_text = generate_captcha_text(captcha_length)
    image.write(captcha_text, save_path)
    data = image.generate(captcha_text)
    return captcha_text


if __name__ == '__main__':
    captcha_text = generate_captcha()
    print('CAPTCHA text:', captcha_text)

    img = Image.open('CAPTCHA.png')
    plt.imshow(img)
    plt.show()