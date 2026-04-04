import streamlit as st
import sys
import os

sys.path.append(".")

from backend.app.main import extract_invoice_data
# from backend.app.main import extract_invoice_data

st.set_page_config(page_title="Invoice Extractor", layout="centered")

st.title("📄 Invoice Data Extractor")
# st.markdown("Upload your invoice PDF and extract key details instantly.")

uploaded_file = st.file_uploader("📂 Upload Invoice PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("✅ PDF Uploaded Successfully")
    save_path = os.path.join("Data",uploaded_file.name)

    if st.button("🚀 Extract Data"):

        with st.spinner("Processing... ⏳"):
            data = extract_invoice_data(uploaded_file)

        # 🔍 SHOW OCR TEXT (Very useful)
        if "raw_text" in data:
            with st.expander("🔍 View OCR Raw Text"):
                st.text(data["raw_text"])

        if "error" in data:
            st.error(data["error"])

        else:
            st.subheader("📊 Extracted Data")

            col1, col2 = st.columns(2)

            with col1:
                st.info(f"🧾 Invoice No: {data.get('invoice_number') or 'Not found'}")
                st.info(f"📅 Date: {data.get('invoice_date') or 'Not found'}")
                st.info(f"👤 Customer: {data.get('customer_name') or 'Not found'}")

            with col2:
                st.info(f"📧 Email: {data.get('email') or 'Not found'}")
                st.info(f"📞 Phone: {data.get('phone_number') or 'Not found'}")
                st.success(f"💰 Total: ₹ {data.get('total_amount') or 'Not found'}")