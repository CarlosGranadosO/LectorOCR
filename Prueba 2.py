from PIL import Image
import pytesseract
#import tesseract
import numpy as np
from deep_translator import GoogleTranslator

######
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
filename = 'image_04.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)

#Esta parte puede detectar idiomas en alfabeto normal lo cual nos hace mas facil pues puedes agregar mas idiomas
traductor = GoogleTranslator(source='auto', target='es')

resultado = traductor.translate(text)

print(text,resultado)