

from pdf2image import convert_from_path
import os

IMAGES_DIR = "/tmp/images"
os.makedirs(IMAGES_DIR, exist_ok=True)

def pdf_to_images(pdf_path):
    try:
        print(f"📄 Converting PDF: {pdf_path}")

        # ✅ DO NOT pass poppler_path
        images = convert_from_path(pdf_path, dpi=300)

        paths = []

        print("📸 Total Images:", len(images))

        for i, img in enumerate(images):
            filename = os.path.basename(pdf_path).replace(".pdf", "")
            out = os.path.join(IMAGES_DIR, f"{filename}_{i}.png")

            img.save(out, "PNG")
            print(f"✅ Saved: {out}")

            paths.append(out)

        return paths

    except Exception as e:
        print("❌ PDF ERROR:", e)
        return []