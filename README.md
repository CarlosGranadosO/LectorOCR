# LectorOCR
Este proyecto implementa un sistema para extraer texto de una imagen utilizando Tesseract OCR y traducirlo al español usando Google Translator.

## Descripción

Este proyecto utiliza la librería Tesseract OCR para reconocer y extraer texto de una imagen. Luego, utiliza Google Translator para traducir el texto extraído al español.

## Características

- Extracción de texto de imágenes usando Tesseract OCR.
- Detección automática del idioma del texto extraído.
- Traducción del texto extraído al español utilizando Google Translator.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/CarlosGranadosO/LectorOCR.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd ExtraccionLectorOCR
    ```

3. Instala las dependencias requeridas:

    ```bash
    pip install -r requirements.txt
    ```

4. Asegúrate de tener Tesseract OCR instalado en tu máquina. Puedes descargarlo desde [aquí](https://github.com/tesseract-ocr/tesseract). Luego, actualiza la ruta a `tesseract.exe` en el script si es necesario.

## Uso

1. Ajusta el archivo de imagen y la ruta a `tesseract.exe` en el script `extraccion_traduccion.py` según tus necesidades:

    ```python
    from PIL import Image
    import pytesseract
    import numpy as np
    from deep_translator import GoogleTranslator

    # Ruta a tesseract.exe
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

    # Nombre del archivo de imagen
    filename = 'image_04.png'

    # Abrir la imagen y convertirla a un array de numpy
    img1 = np.array(Image.open(filename))

    # Extraer texto de la imagen
    text = pytesseract.image_to_string(img1)

    # Traducir el texto extraído al español
    traductor = GoogleTranslator(source='auto', target='es')
    resultado = traductor.translate(text)

    # Imprimir el texto original y traducido
    print(text, resultado)
    ```

2. Ejecuta el script:

    ```bash
    python LectorOCR.py
    ```

3. Observa el texto extraído y traducido en la consola.
   
