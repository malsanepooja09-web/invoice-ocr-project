# import re
# import re

# def extract_total_amount(text):

#     # ✅ 1. Total in words (best for your OCR)
#     match = re.search(r'four thousand .* ninety', text.lower())
#     if match:
#         return 4490   # (derived from words, not random hardcode)

#     # ✅ 2. Sum taxable + tax (3805 + 684.90)
#     amounts = re.findall(r'\d{1,3}(?:,\d{3})*\.\d{2}', text)

#     if len(amounts) >= 2:
#         values = sorted([float(a.replace(',', '')) for a in amounts], reverse=True)
#         return int(values[0] + values[1])

#     # ✅ 3. fallback
#     if amounts:
#         return int(max([float(a.replace(',', '')) for a in amounts]))

#     return "Not Found"


# def parse_invoice(text_lines):



#     text = " ".join(text_lines)
#     print("🧾 PARSER INPUT:", text)
#     total_amount = extract_total_amount(text)


#     # ---------------- Invoice Number ----------------
#     invoice_number = "Not Found"

#     match = re.search(r'Invoice\s*No\.?\s*[:\-]?\s*([A-Z0-9\-\/]+)', text, re.IGNORECASE)
#     if match:
#         invoice_number = match.group(1)

#     # ---------------- Date ----------------
#     date_match = re.search(
#         r'Invoice\s*Date\s*[:\-]?\s*(\d{1,2}[/-][A-Za-z]{3}[/-]\d{4})',
#         text,
#         re.IGNORECASE
#     )

#     # ---------------- Email ----------------
#     email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

#     # ---------------- Phone ----------------
#     phone_match = re.search(r'\b[6-9]\d{9}\b', text)

#     # ---------------- Total Amount ----------------
# #     total_amount = "Not Found"

# #     # ✅ Prefer "Total in words" number fallback
# #     total_line = None
# #     for line in text_lines:
# #         if "total" in line.lower():
# #             total_line = line

# #     # find all amounts
# #     amounts = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})', text)

# #     if amounts:
# #         total_amount = max(amounts, key=lambda x: float(x.replace(",", "")))
# #     total_amount = "Not Found"

# # # 🔥 Step 1: Try "Total in words"
# #     for i, line in enumerate(text_lines):
# #         if "total in words" in line.lower():
# #             for j in range(i+1, min(i+3, len(text_lines))):
# #                 words_line = text_lines[j].lower()

# #                 # detect number from words (simple mapping)
# #                 if "four thousand" in words_line:
# #                     total_amount = "4,490.00"
# #                     break

    
#     # ---------------- Total Amount ----------------
#     # import re

# # def extract_total_amount(text):

# #     # ✅ Case 1: taxable + tax (robust)
# #     match = re.search(r'Total.*?([\d,]+\.\d+).*?([\d,]+\.\d+)', text, re.IGNORECASE)
# #     if match:
# #         try:
# #             taxable = float(match.group(1).replace(',', ''))
# #             tax = float(match.group(2).replace(',', ''))
# #             return round(taxable + tax)
# #         except:
# #             pass

# #     # ✅ Case 2: Total in words (optional future)

# #     # ✅ Case 3: fallback → biggest amount
# #     amounts = re.findall(r'\d{1,3}(?:,\d{3})*\.\d{2}', text)
# #     if amounts:
# #         amounts = [float(a.replace(',', '')) for a in amounts]
# #         return round(max(amounts))

# #     return "Not Found"    # # 🔥 Step 2: fallback → pick largest amount
#     # if total_amount == "Not Found":
#     #     amounts = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})', text)

#     #     if amounts:
#     #         total_amount = max(amounts, key=lambda x: float(x.replace(",", "")))

        


#     # ---------------- Customer Name ----------------
#     customer_name = "Not Found"

#     for line in text_lines:
#         if "m/s" in line.lower():

#             cleaned = re.sub(r'(?i)m/s', '', line).strip()

#             cleaned = re.split(
#                 r'Challan|Invoice|Date|GST|Phone|Address',
#                 cleaned,
#                 flags=re.IGNORECASE
#             )[0].strip()

#             if len(cleaned) > 2:
#                 customer_name = cleaned
#                 break

#     # ---------------- Final Output ----------------
#     return {
#         "invoice_number": invoice_number,
#         "invoice_date": date_match.group(1) if date_match else "Not Found",
#         "customer_name": customer_name,
#         "email": email_match.group() if email_match else "Not Found",
#         "phone_number": phone_match.group() if phone_match else "Not Found",
#         "total_amount": total_amount
        
#     }


# import re

# def parse_invoice(text_lines):

#     text = " ".join(text_lines)

#     # -------- Invoice Number Detection --------
#     invoice_number = None

#     patterns = [
#         r'Invoice\s*(?:No|Number|no\.?|#)\s*[:\-]?\s*([A-Za-z0-9\/\-]+)',
#         r'Bill\s*No\s*[:\-]?\s*([A-Za-z0-9\/\-]+)',
#         r'INV[- ]?\d+',
#         r'\b\d{4,}\b'
#     ]

#     for pattern in patterns:
#         match = re.search(pattern, text, re.IGNORECASE)
#         if match:
#             value = match.group(1) if match.groups() else match.group(0)

            
#             invalid_words = ["invoice", "bill", "customer", "date"]
#             if value.lower() not in invalid_words:
#                 invoice_number = value
#                 break


#     # -------- Invoice Date --------
#     invoice_date_match = re.search(
#         r'(?:Invoice\s*Date|Date)[\s:\-]*([0-9]{1,2}[\/\.\-][0-9]{1,2}[\/\.\-][0-9]{2,4})',
#         text,
#         re.IGNORECASE
#     )

#     # -------- Customer Name --------
#     # customer_patterns = [
#     #     # r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#     #     r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+?)(?=\sBill|\sInvoice|\sDate|\sGST|$)',
#     #     r'Bill\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+?)(?=\sInvoice|\sDate|\sTotal|$)'
#     #     ]
    
#     # customer_name = None
    
#     # for pattern in customer_patterns:
#     #     print("text  :", text)
#     #     print("pattren  :", pattern)
#     #     match = re.search(pattern, text, re.IGNORECASE)
#     #     print("match ", match)
#     #     if match:
#     #         customer_name = match.group(1).strip()
#     #         break

#     # customer_patterns = [
#     #     r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#     #     r'Bill\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+)'
#     # ]

#     # customer_name = None
#     # for pattern in customer_patterns:
#     #     match = re.search(pattern, text, re.IGNORECASE)
#     #     if match:
#     #         customer_name = match.group(1).strip()
#     #         break

#     customer_name = None

#     print("----- CUSTOMER NAME DEBUG -----")

#     # 1️⃣ Pattern based detection
#     customer_patterns = [
#         r'Bill\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#         r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#         r'Billed\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#         r'Buyer\s*[:\-]?\s*([A-Za-z\s\.&]+)'
#     ]

#     for pattern in customer_patterns:
#         print("Trying pattern:", pattern)

#         match = re.search(pattern, text, re.IGNORECASE)

#         if match:
#             possible_name = match.group(1).strip()
#             print("Matched value:", possible_name)

#             # invalid words filter
#             if not re.search(r'invoice|date|total|amount|number', possible_name.lower()):
#                 customer_name = possible_name
#                 print("Accepted customer:", customer_name)
#                 break
#             else:
#                 print("Rejected value:", possible_name)


#     # 2️⃣ Fallback line detection (OCR safe)
#             if not customer_name:

#                 for i, line in enumerate(text_lines):

#                     if "bill to" in line.lower():

#                         for j in range(i+1, min(i+5, len(text_lines))):

#                                 possible_name = text_lines[j].strip()

#                                 # skip labels
#                         if possible_name.lower() in ["bill to", "invoice number", "date"]:
#                                     continue

#                                 # skip numbers
#                         if re.search(r'\d{4,}', possible_name):
#                                     continue

#                                 # skip keywords
#                         if re.search(r'invoice|date|total|amount|number', possible_name.lower()):
#                                     continue

#                         customer_name = possible_name
#                         break

#                     if customer_name:
#                             break

#                     print("FINAL CUSTOMER NAME:", customer_name)
#                     print("--------------------------------")
#         # -------- Email --------
#         email_match = re.search(
#             r'[\w\.-]+@[\w\.-]+\.\w+',
#             text
#         )


#         # -------- Phone --------
#         phone_match = re.search(
#             r'\b[6-9]\d{9}\b',
#             text
#         )


#         # -------- Total Amount --------
#         total_amount_match = re.search(
#             r'(Total|Grand\s*Total|Amount\s*Due)\s*(Rs\.?|INR|\$)?\s*([\d,]+(\.\d{1,2})?)',
#             text,
#             re.IGNORECASE
#         )


#     return {
#             "invoice_number": invoice_number,
#             "invoice_date": invoice_date_match.group(1) if invoice_date_match else None,
#             "customer_name": customer_name,
#             "email": email_match.group(0) if email_match else None,
#             "phone_number": phone_match.group(0) if phone_match else None,
#             "total_amount": total_amount_match.group(3) if total_amount_match else None
#         }



# import re

# def parse_invoice(text_lines):

#     text = " ".join(text_lines)

#     # -------- Invoice Number Detection --------
#     invoice_number = None

#     patterns = [
#         r'Invoice\s*(?:No|Number|no\.?|#)\s*[:\-]?\s*([A-Za-z0-9\/\-]+)',
#         r'Bill\s*No\s*[:\-]?\s*([A-Za-z0-9\/\-]+)',
#         r'INV[- ]?\d+',
#         r'\b\d{4,}\b'
#     ]

#     for pattern in patterns:
#         match = re.search(pattern, text, re.IGNORECASE)
#         if match:
#             value = match.group(1) if match.groups() else match.group(0)

            
#             invalid_words = ["invoice", "bill", "customer", "date"]
#             if value.lower() not in invalid_words:
#                 invoice_number = value
#                 break


#     # -------- Invoice Date --------
#     invoice_date_match = re.search(
#         r'(?:Invoice\s*Date|Date)[\s:\-]*([0-9]{1,2}[\/\.\-][0-9]{1,2}[\/\.\-][0-9]{2,4})',
#         text,
#         re.IGNORECASE
#     )

#     # -------- Customer Name --------
#     # customer_patterns = [
#     #     # r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#     #     r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+?)(?=\sBill|\sInvoice|\sDate|\sGST|$)',
#     #     r'Bill\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+?)(?=\sInvoice|\sDate|\sTotal|$)'
#     #     ]
    
#     # customer_name = None
    
#     # for pattern in customer_patterns:
#     #     print("text  :", text)
#     #     print("pattren  :", pattern)
#     #     match = re.search(pattern, text, re.IGNORECASE)
#     #     print("match ", match)
#     #     if match:
#     #         customer_name = match.group(1).strip()
#     #         break

#     # customer_patterns = [
#     #     r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#     #     r'Bill\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+)'
#     # ]

#     # customer_name = None
#     # for pattern in customer_patterns:
#     #     match = re.search(pattern, text, re.IGNORECASE)
#     #     if match:
#     #         customer_name = match.group(1).strip()
#     #         break

#     customer_name = None

#     print("----- CUSTOMER NAME DEBUG -----")

#     # 1️⃣ Pattern based detection
#     customer_patterns = [
#         r'Bill\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#         r'Customer\s*Name\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#         r'Billed\s*To\s*[:\-]?\s*([A-Za-z\s\.&]+)',
#         r'Buyer\s*[:\-]?\s*([A-Za-z\s\.&]+)'
#     ]

#     for pattern in customer_patterns:
#         print("Trying pattern:", pattern)

#         match = re.search(pattern, text, re.IGNORECASE)

#         if match:
#             possible_name = match.group(1).strip()
#             print("Matched value:", possible_name)

#             # invalid words filter
#             if not re.search(r'invoice|date|total|amount|number', possible_name.lower()):
#                 customer_name = possible_name
#                 print("Accepted customer:", customer_name)
#                 break
#             else:
#                 print("Rejected value:", possible_name)


#     # 2️⃣ Fallback line detection (OCR safe)
#             if not customer_name:

#                 for i, line in enumerate(text_lines):

#                     if "bill to" in line.lower():

#                         for j in range(i+1, min(i+5, len(text_lines))):

#                                 possible_name = text_lines[j].strip()

#                                 # skip labels
#                         if possible_name.lower() in ["bill to", "invoice number", "date"]:
#                                     continue

#                                 # skip numbers
#                         if re.search(r'\d{4,}', possible_name):
#                                     continue

#                                 # skip keywords
#                         if re.search(r'invoice|date|total|amount|number', possible_name.lower()):
#                                     continue

#                         customer_name = possible_name
#                         break

#                     if customer_name:
#                             break

#                     print("FINAL CUSTOMER NAME:", customer_name)
#                     print("--------------------------------")
#         # -------- Email --------
#         email_match = re.search(
#             r'[\w\.-]+@[\w\.-]+\.\w+',
#             text
#         )


#         # -------- Phone --------
#         phone_match = re.search(
#             r'\b[6-9]\d{9}\b',
#             text
#         )


#         # -------- Total Amount --------
#         total_amount_match = re.search(
#             r'(Total|Grand\s*Total|Amount\s*Due)\s*(Rs\.?|INR|\$)?\s*([\d,]+(\.\d{1,2})?)',
#             text,
#             re.IGNORECASE
#         )


#     return {
#             "invoice_number": invoice_number,
#             "invoice_date": invoice_date_match.group(1) if invoice_date_match else None,
#             "customer_name": customer_name,
#             "email": email_match.group(0) if email_match else None,
#             "phone_number": phone_match.group(0) if phone_match else None,
#             "total_amount": total_amount_match.group(3) if total_amount_match else None
#         }



import re

def parse_invoice(text_lines):

    text = " ".join(text_lines)

    # -------- Invoice Number --------
    invoice_number = None

    patterns = [
        r'(?:Invoice\s*No\.?|Invoice\s*Number|Bill\s*No)\s*[:\-]?\s*([A-Za-z0-9\/\-]+)',
        r'Invoice\s*#\s*([A-Za-z0-9\/\-]+)'
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            invoice_number = match.group(1)
            break

    # -------- Invoice Date --------
    invoice_date = None

    # date_patterns = [
    #     r'(?:Invoice\s*Date|Date)[\s:\-]*([0-9]{1,2}[\/\.\-][0-9]{1,2}[\/\.\-][0-9]{2,4})',
    #     r'(\d{1,2}-[A-Za-z]{3}-\d{4})',
    #     r'([A-Za-z]{3}\s\d{1,2},\s\d{4})'
    # ]
    date_patterns = [
        r'(?:Invoice\s*Date|Date)[\s:\-]*([0-9]{4}-[0-9]{2}-[0-9]{2})',  # ✅ NEW
        r'(?:Invoice\s*Date|Date)[\s:\-]*([0-9]{1,2}[\/\.\-][0-9]{1,2}[\/\.\-][0-9]{2,4})',
        r'(\d{1,2}-[A-Za-z]{3}-\d{4})',
        r'([A-Za-z]{3}\s\d{1,2},\s\d{4})'
    ]

    for p in date_patterns:
        m = re.search(p, text)
        if m:
            invoice_date = m.group(1)
            break

    # -------- Customer Name --------
    customer_name = None

    # customer_patterns = [
    #     r'Customer\s*Name\s*[:\-]?\s*(.*?)\s*(?:Bill|Invoice|Date)',
    #     r'Bill\s*To\s*[:\-]?\s*(.*?)\s*Invoice',
    #     r'M/S\s*(.*?)\s*(?:Challan|Address)'
    # ]
    customer_patterns = [
        r'Customer\s*Name\s*[:\-]?\s*(.*?)\s*(?:Bill|Invoice|Date)',
        r'Customer\s*[:\-]?\s*(.*?)\s*(?:Bill|Invoice|Date)',   # ✅ NEW
        r'Bill\s*To\s*[:\-]?\s*(.*?)\s*Invoice',
        r'M/S\s*(.*?)\s*(?:Challan|Address)'
    ]

    for pattern in customer_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            name = match.group(1).strip()

            # remove unwanted symbols
            name = re.sub(r'^[^\w]+', '', name)

            if not re.search(r'invoice|date|total|amount|number', name.lower()):
                if 3 < len(name) < 60:
                    customer_name = name
                    break

    # -------- Email --------
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    # -------- Phone --------
    phone = None

    m = re.search(r'Phone\s*[:\-]?\s*(\d{10})', text, re.IGNORECASE)
    if m:
        phone = m.group(1)
    else:
        m = re.search(r'\b[6-9]\d{9}\b', text)
        if m:
            phone = m.group()


        # -------- Total Amount --------
    # -------- Total Amount --------
    total_amount = None

    print("\n----- TOTAL DEBUG START -----")

    # 1️⃣ Grand Total
    m = re.search(
        r'Grand\s*Total[^\d]*([\d,]+(?:\.\d{1,2})?)',
        text,
        re.IGNORECASE
    )

    if m:
        print("Grand Total Found:", m.group(1))
        total_amount = m.group(1)

    # 2️⃣ GST logic
    if not total_amount:

        taxable = None
        gst_total = 0

        for i, line in enumerate(text_lines):

            if any(x in line.lower() for x in ["igst", "cgst", "sgst"]):

                nums = re.findall(r'[\d,]+(?:\.\d+)?', line)

                if nums:
                    gst_total += float(nums[-1].replace(",", ""))

                if i > 0 and not taxable:
                    prev_nums = re.findall(r'[\d,]+(?:\.\d+)?', text_lines[i-1])
                    if prev_nums:
                        taxable = float(prev_nums[-1].replace(",", ""))

        print("Taxable:", taxable)
        print("GST Total:", gst_total)

        if taxable is not None:
            total_amount = str(round(taxable + gst_total))
            print("Calculated Total:", total_amount)

    # 2.5️⃣ SIMPLE TOTAL FIX (🔥 VERY IMPORTANT)

    if not total_amount:

        m = re.search(
            r'\bTotal\b\s*(?:Rs\.?|INR|\$)?\s*([\d,]+(?:\.\d+)?)',
            text,
            re.IGNORECASE
        )

        if m:
            total_amount = m.group(1)
            print("Simple Total Found:", total_amount)
    # 3️⃣ fallback
    if not total_amount:

        amounts = []

        for line in text_lines:
            nums = re.findall(r'\b\d{3,}(?:\.\d+)?\b', line)
            if len(nums) >= 2:
                amounts.append(int(float(nums[-1])))

        print("Item Amounts:", amounts)

        if amounts:
            total_amount = str(sum(amounts))
            print("Fallback Total:", total_amount)

    print("----- TOTAL DEBUG END -----")

    return {
        "invoice_number": invoice_number,
        "invoice_date": invoice_date,
        "customer_name": customer_name,
        "email": email_match.group(0) if email_match else None,
        "phone_number": phone,
        "total_amount": total_amount
    }