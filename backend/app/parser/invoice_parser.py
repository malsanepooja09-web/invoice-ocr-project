# import re

# def parse_invoice(text_lines):

#     text = " ".join(text_lines)

#     print("🔍 OCR TEXT:", text)

#     print("🧾 PARSER INPUT:", text)


#     # ---------------- Invoice Number (SUPER ROBUST) ----------------

#     invoice_number = "Not Found"

#     patterns = [
#         r'Invoice\s*(No|Number)?\s*[:#\-]?\s*(\d+)',
#         r'Bill\s*(No)?\s*[:#\-]?\s*(\d+)',
#         r'Ref\s*(No)?\s*[:#\-]?\s*(\d+)',
#         r'\bINV[- ]?(\d+)\b'
#     ]

#     for pattern in patterns:
#         match = re.search(pattern, text, re.IGNORECASE)
#         if match:
#             invoice_number = match.group(match.lastindex)
#             break

#     # fallback (last option)
#     if invoice_number == "Not Found":
#         match = re.search(r'\b\d{5,}\b', text)
#         if match:
#             invoice_number = match.group()

#     # invoice_number = "Not Found"

#     # # Try line by line (BEST method)
#     # for line in text_lines:
#     #     line_lower = line.lower()
        
#     #     if "invoice" in line_lower:
#     #         match = re.search(r'\d{4,}', line)  # any number >= 4 digits
#     #         if match:
#     #             invoice_number = match.group()
#     #             break


#     # # Fallback (full text search)
#     # if invoice_number == "Not Found":
#     #     match = re.search(r'\b\d{5,}\b', text)
#     #     if match:
#     #         invoice_number = match.group()



#     # ---------------- Invoice Number ----------------
    
#     # invoice_number = None

#     # patterns = [
#     #     r'Invoice\s*(No|Number)?[:\-]?\s*(\d+)',
#     #     r'Bill\s*No[:\-]?\s*(\d+)'
#     # ]

#     # for pattern in patterns:
#     #     match = re.search(pattern, text, re.IGNORECASE)
#     #     if match:
#     #         invoice_number = match.group(match.lastindex)
#     #         break

#     # ---------------- Date ----------------
#     date_match = re.search(
#         r'(?:Invoice\s*Date|Date)?[\s:\-]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})',
#         text,
#         re.IGNORECASE
#     )

#     # ---------------- Email ----------------
#     email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

#     # ---------------- Phone ----------------
#     phone_match = re.search(r'\b[6-9]\d{9}\b', text)

#     # ---------------- Amount ----------------
#     amount_match = re.search(
#         r'(Total|Grand\s*Total|Amount\s*Due)[^\d]*(\d{1,3}(,\d{3})*(\.\d+)?)',
#         text,
#         re.IGNORECASE
#     )

#     # ---------------- Customer Name ----------------
#     customer_name = "Not Found"

#     # ✅ Case 1: Same line
#     for line in text_lines:
#         if "bill to" in line.lower():

#             cleaned = re.sub(r'(?i)bill\s*to', '', line).strip()
#             cleaned = re.split(r'Invoice|Date|Total', cleaned, flags=re.IGNORECASE)[0].strip()
#             cleaned = re.sub(r'\d+', '', cleaned).strip()

#             if len(cleaned) > 2:
#                 customer_name = cleaned
#                 break

#     # ✅ Case 2: Next lines fallback
#     if customer_name == "Not Found":
#         for i, line in enumerate(text_lines):
#             if "bill to" in line.lower():

#                 for j in range(i + 1, min(i + 5, len(text_lines))):
#                     candidate = text_lines[j].strip()

#                     if any(word in candidate.lower() for word in ["invoice", "date", "total"]):
#                         continue

#                     if len(candidate) > 2 and not re.search(r'\d', candidate):
#                         customer_name = candidate
#                         break

#                 if customer_name != "Not Found":
#                     break

#     # ---------------- Final Output ----------------
#     return {
#         "invoice_number": invoice_number or "Not Found",
#         "invoice_date": date_match.group(1) if date_match else "Not Found",
#         "customer_name": customer_name,
#         "email": email_match.group() if email_match else "Not Found",
#         "phone_number": phone_match.group() if phone_match else "Not Found",
#         "total_amount": amount_match.group(2) if amount_match else "Not Found"
#     }


# # import re

# # def parse_invoice(text_lines):

# #     text = " ".join(text_lines)
# #     print("🔍 OCR TEXT:", text)

# #     # ---------------- Invoice Number ----------------
# #     invoice_number = "Not Found"

# #     patterns = [
# #         r'Invoice\s*(No|Number)?\s*[:#\-]?\s*([A-Za-z0-9\-\/]+)',
# #         r'Bill\s*(No)?\s*[:#\-]?\s*([A-Za-z0-9\-\/]+)',
# #         r'Ref\s*(No)?\s*[:#\-]?\s*([A-Za-z0-9\-\/]+)',
# #         r'\bINV[- ]?([A-Za-z0-9\-]+)\b'
# #     ]

# #     for pattern in patterns:
# #         match = re.search(pattern, text, re.IGNORECASE)
# #         if match:
# #             invoice_number = match.group(match.lastindex)
# #             break

# #     # fallback (keep your logic, just improved)
# #     if invoice_number == "Not Found":
# #         match = re.search(r'\b[A-Za-z0-9\-]{5,}\b', text)
# #         if match:
# #             invoice_number = match.group()

# #     # ---------------- Date ----------------
# #     date_match = re.search(
# #         r'(?:Invoice\s*Date|Date)?[\s:\-]*('
# #         r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|'
# #         r'\d{1,2}[-/][A-Za-z]{3}[-/]\d{4}'
# #         r')',
# #         text,
# #         re.IGNORECASE
# #     )

# #     # ---------------- Email ----------------
# #     email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

# #     # ---------------- Phone ----------------
# #     phone_match = re.search(r'\b[6-9]\d{9}\b', text)

# #     # ---------------- Amount ----------------
# #     amount_match = re.search(
# #         r'(Total|Grand\s*Total|Amount\s*Due)?[^\d₹]*₹?\s*(\d{1,3}(,\d{3})*(\.\d{2}))',
# #         text,
# #         re.IGNORECASE
# #     )

# #     # ---------------- Customer Name ----------------
# #     customer_name = "Not Found"

# #     # ✅ keep your Bill To logic
# #     for line in text_lines:
# #         if "bill to" in line.lower():

# #             cleaned = re.sub(r'(?i)bill\s*to', '', line).strip()
# #             cleaned = re.split(r'Invoice|Date|Total', cleaned, flags=re.IGNORECASE)[0].strip()
# #             cleaned = re.sub(r'\d+', '', cleaned).strip()

# #             if len(cleaned) > 2:
# #                 customer_name = cleaned
# #                 break

# #     # ✅ fallback (same structure, improved coverage)
# #     if customer_name == "Not Found":
# #         for i, line in enumerate(text_lines):
# #             if any(keyword in line.lower() for keyword in ["bill to", "ship to", "m/s"]):

# #                 # try same line
# #                 cleaned = re.sub(r'(?i)(bill\s*to|ship\s*to|m/s)', '', line).strip()
# #                 cleaned = re.sub(r'\d+', '', cleaned).strip()

# #                 if len(cleaned) > 2:
# #                     customer_name = cleaned
# #                     break

# #                 # try next lines
# #                 for j in range(i + 1, min(i + 5, len(text_lines))):
# #                     candidate = text_lines[j].strip()

# #                     if any(word in candidate.lower() for word in ["invoice", "date", "total"]):
# #                         continue

# #                     if len(candidate) > 2 and not re.search(r'\d', candidate):
# #                         customer_name = candidate
# #                         break

# #                 if customer_name != "Not Found":
# #                     break

# #     # ---------------- Final Output ----------------
# #     return {
# #         "invoice_number": invoice_number,
# #         "invoice_date": date_match.group(1) if date_match else "Not Found",
# #         "customer_name": customer_name,
# #         "email": email_match.group() if email_match else "Not Found",
# #         "phone_number": phone_match.group() if phone_match else "Not Found",
# #         "total_amount": amount_match.group(2) if amount_match else "Not Found"
# #     }


import re
# import re

def extract_total_amount(text):

    # ✅ Case 1: subtotal + tax
    match = re.search(r'([\d,]+\.\d+).*?IGST.*?([\d,]+\.\d+)', text, re.IGNORECASE)

    if match:
        try:
            subtotal = float(match.group(1).replace(',', ''))
            tax = float(match.group(2).replace(',', ''))
            return round(subtotal + tax)
        except:
            pass

    # ✅ Case 2: fallback (last big amount)
    amounts = re.findall(r'[\d,]+\.\d+', text)

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