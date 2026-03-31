import streamlit as st
import sys
# import sys
import os

sys.path.append(os.path.abspath("."))

# sys.path.append(".")

from backend.app.main import extract_invoice_data

st.set_page_config(page_title="Invoice Extractor", layout="centered")

st.title("📄 Invoice Data Extractor")

uploaded_file = st.file_uploader("Upload Invoice PDF", type=["pdf"])

if uploaded_file is not None:

    st.success("✅ PDF Uploaded")

    # if st.button("Extract Data"):
        

    #     with st.spinner("Processing... ⏳"):
    #         data = extract_invoice_data(uploaded_file)
    #         if "raw_text" in data:
    #             st.subheader("🔍 OCR RAW TEXT")
    #             st.text(data["raw_text"])

    #         data = extract_invoice_data(uploaded_file)

    #     if "error" in data:
    #         st.error(data["error"])
    #     else:
    #         st.subheader("📊 Extracted Data")


    #         st.write("Invoice Number:", data["invoice_number"])
    #         st.write("Invoice Date:", data["invoice_date"])
    #         st.write("Customer Name:", data["customer_name"])
    #         st.write("Email:", data["email"])
    #         st.write("Phone:", data["phone_number"])
    #         st.write("Total Amount:", data["total_amount"])


    #         # st.write("Invoice Number:", data["invoice_number"])
    #         # st.write("Invoice Date:", data["invoice_date"])
    #         # st.write("Customer Name:", data["customer_name"])
    #         # st.write("Email:", data["email"])
    #         # st.write("Phone:", data["phone_number"])
    #         # st.write("Total Amount:", data["total_amount"])
    if st.button("Extract Data"):

        with st.spinner("Processing... ⏳"):
            data = extract_invoice_data(uploaded_file)
            st.write("DEBUG DATA:", data)

        # # 👇 ALWAYS show (no condition)
        # st.subheader("🔍 OCR RAW TEXT")
        # st.text(data.get("raw_text", "No OCR text found"))

        if "error" in data:
            st.error(data["error"])
        else:
            st.subheader("📊 Extracted Data")

            # st.write("Invoice Number:", data["invoice_number"])
            # st.write("Invoice Date:", data["invoice_date"])
            # st.write("Customer Name:", data["customer_name"])
            # st.write("Email:", data["email"])
            # st.write("Phone:", data["phone_number"])
            # st.write("Total Amount:", data["total_amount"])


            st.write("Invoice Number:", data.get("invoice_number", "Not found"))
            st.write("Invoice Date:", data.get("invoice_date", "Not found"))
            st.write("Customer Name:", data.get("customer_name", "Not found"))
            st.write("Email:", data.get("email", "Not found"))
            st.write("Phone:", data.get("phone_number", "Not found"))
            st.write("Total Amount:", data.get("total_amount", "Not found"))