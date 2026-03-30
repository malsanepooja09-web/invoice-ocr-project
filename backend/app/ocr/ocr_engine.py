import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from dotenv import load_dotenv

import os

# ✅ load env
load_dotenv()

# ✅ get path from .env
tesseract_path = os.getenv("TESSERACT_PATH")

# ✅ set path
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# print(pytesseract.get_tesseract_version())


# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"
# import pytesseract
print(pytesseract.get_tesseract_version())

def extract_text(image_path):
    try:
        print("📄 Processing Image:", image_path)
        img = Image.open(image_path)

        # 🔥 Improve OCR accuracy
        img = img.convert("L")  # grayscale
        img = img.filter(ImageFilter.SHARPEN)
        

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2)

        print("📄 Processing Image:", image_path)  
        text = pytesseract.image_to_string(img)
        # print("🔍 RAW OCR TEXT:", text)

        print("🔍 OCR RAW TEXT:\n", text)

        text_list = text.split("\n")
        print("📝 TEXT LINES:", text_list)
        cleaned = [line.strip() for line in text_list if line.strip()]

        return cleaned

    except Exception as e:
        print("❌ OCR ERROR:", e)
        return []






















# import pytesseract
# from PIL import Image

# def extract_text(image_path):
#     try:
#         img = Image.open(image_path)

#         text = pytesseract.image_to_string(img)

#         text_list = text.split("\n")
#         print("🔍 OCR RAW TEXT:\n", text)

#         cleaned = [line.strip() for line in text_list if line.strip()]

#         print("✅ OCR TEXT:", cleaned)

#         return cleaned

#     except Exception as e:
#         print("❌ OCR ERROR:", e)
#         return []