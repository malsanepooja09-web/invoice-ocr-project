import re
import re

def extract_total_amount(text):

    lines = text.split('\n')

    # ✅ STEP 1: Find ₹ amounts (BEST)
    rupee_matches = re.findall(r'₹\s*([\d,]+\.\d{2})', text)
    if rupee_matches:
        return int(float(rupee_matches[-1].replace(',', '')))

    # ✅ STEP 2: Find "Total" block (STRICT)
    for i, line in enumerate(lines):
        if "total" in line.lower():

            # check next 5 lines ONLY
            for j in range(i, min(i+5, len(lines))):

                # skip tax lines
                if "tax" in lines[j].lower():
                    continue

                match = re.search(r'([\d,]+\.\d{2})', lines[j])
                if match:
                    value = float(match.group(1).replace(',', ''))

                    # ignore small values (like 2535, 1270 etc.)
                    if value > 1000:   # threshold
                        return int(value)

    # ✅ STEP 3: fallback → max
    amounts = re.findall(r'\d{1,3}(?:,\d{3})*\.\d{2}', text)
    if amounts:
        values = [float(a.replace(',', '')) for a in amounts]
        return int(max(values))

    return "Not Found"


def parse_invoice(text_lines):



    text = " ".join(text_lines)
    print("🧾 PARSER INPUT:", text)
    total_amount = extract_total_amount(text)


    # ---------------- Invoice Number ----------------
    invoice_number = "Not Found"

    match = re.search(r'Invoice\s*No\.?\s*[:\-]?\s*([A-Z0-9\-\/]+)', text, re.IGNORECASE)
    if match:
        invoice_number = match.group(1)

    # ---------------- Date ----------------
    date_match = re.search(
        r'Invoice\s*Date\s*[:\-]?\s*(\d{1,2}[/-][A-Za-z]{3}[/-]\d{4})',
        text,
        re.IGNORECASE
    )

    # ---------------- Email ----------------
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    # ---------------- Phone ----------------
    phone_match = re.search(r'\b[6-9]\d{9}\b', text)

    # ---------------- Total Amount ----------------
#     total_amount = "Not Found"

#     # ✅ Prefer "Total in words" number fallback
#     total_line = None
#     for line in text_lines:
#         if "total" in line.lower():
#             total_line = line

#     # find all amounts
#     amounts = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})', text)

#     if amounts:
#         total_amount = max(amounts, key=lambda x: float(x.replace(",", "")))
#     total_amount = "Not Found"

# # 🔥 Step 1: Try "Total in words"
#     for i, line in enumerate(text_lines):
#         if "total in words" in line.lower():
#             for j in range(i+1, min(i+3, len(text_lines))):
#                 words_line = text_lines[j].lower()

#                 # detect number from words (simple mapping)
#                 if "four thousand" in words_line:
#                     total_amount = "4,490.00"
#                     break

    
    # ---------------- Total Amount ----------------
    # import re

# def extract_total_amount(text):

#     # ✅ Case 1: taxable + tax (robust)
#     match = re.search(r'Total.*?([\d,]+\.\d+).*?([\d,]+\.\d+)', text, re.IGNORECASE)
#     if match:
#         try:
#             taxable = float(match.group(1).replace(',', ''))
#             tax = float(match.group(2).replace(',', ''))
#             return round(taxable + tax)
#         except:
#             pass

#     # ✅ Case 2: Total in words (optional future)

#     # ✅ Case 3: fallback → biggest amount
#     amounts = re.findall(r'\d{1,3}(?:,\d{3})*\.\d{2}', text)
#     if amounts:
#         amounts = [float(a.replace(',', '')) for a in amounts]
#         return round(max(amounts))

#     return "Not Found"    # # 🔥 Step 2: fallback → pick largest amount
    # if total_amount == "Not Found":
    #     amounts = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})', text)

    #     if amounts:
    #         total_amount = max(amounts, key=lambda x: float(x.replace(",", "")))

        


    # ---------------- Customer Name ----------------
    customer_name = "Not Found"

    for line in text_lines:
        if "m/s" in line.lower():

            cleaned = re.sub(r'(?i)m/s', '', line).strip()

            cleaned = re.split(
                r'Challan|Invoice|Date|GST|Phone|Address',
                cleaned,
                flags=re.IGNORECASE
            )[0].strip()

            if len(cleaned) > 2:
                customer_name = cleaned
                break

    # ---------------- Final Output ----------------
    return {
        "invoice_number": invoice_number,
        "invoice_date": date_match.group(1) if date_match else "Not Found",
        "customer_name": customer_name,
        "email": email_match.group() if email_match else "Not Found",
        "phone_number": phone_match.group() if phone_match else "Not Found",
        "total_amount": total_amount
        
    }