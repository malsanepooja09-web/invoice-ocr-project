import os

from backend.app.ocr.pdf_to_image import pdf_to_images
from backend.app.ocr.ocr_engine import extract_text
from backend.app.parser.invoice_parser import parse_invoice

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_invoice_data(uploaded_file):

    try:
        file_location = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

        with open(file_location, "wb") as buffer:
            buffer.write(uploaded_file.getbuffer())

        print(f"📂 PDF Saved: {file_location}")

        images = pdf_to_images(file_location)

        all_text = []

        for img_path in images:
            text = extract_text(img_path)
            all_text.extend(text)

        print("📝 FINAL OCR TEXT:", all_text)

        invoice_data = parse_invoice(all_text)

        print("✅ FINAL DATA:", invoice_data)

        return invoice_data

    except Exception as e:
        print("❌ MAIN ERROR:", e)
        return {"error": str(e)}