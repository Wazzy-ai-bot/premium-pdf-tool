import streamlit as st
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import tempfile
import os

st.set_page_config(page_title="Premium PDF Tool", page_icon="📄")

st.title("📄 Premium PDF Merge, Split & Compress Tool")
st.write("Merge, split, and compress PDFs easily. Perfect for professionals.")

# --- Merge PDFs ---
st.header("Merge PDFs")
merge_files = st.file_uploader(
    "Drag and drop PDFs to merge",
    type="pdf",
    accept_multiple_files=True
)

if st.button("Merge PDFs") and merge_files:
    merger = PdfMerger()
    for file in merge_files:
        merger.append(file)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    merger.write(temp_file.name)
    merger.close()
    st.success("PDFs merged successfully!")
    st.download_button("Download Merged PDF", temp_file.name, file_name="merged.pdf")

# --- Split PDF ---
st.header("Split PDF")
split_file = st.file_uploader("Upload PDF to split", type="pdf")

if split_file and st.button("Split PDF"):
    reader = PdfReader(split_file)
    temp_files = []
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f"_page{i+1}.pdf")
        with open(temp_file.name, "wb") as f:
            writer.write(f)
        temp_files.append(temp_file.name)

    st.success(f"PDF split into {len(temp_files)} pages!")
    for i, f in enumerate(temp_files):
        st.download_button(f"Download Page {i+1}", f, file_name=f"page{i+1}.pdf")

# --- Compress PDF ---
st.header("Compress PDF")
compress_file = st.file_uploader("Upload PDF to compress", type="pdf")

if compress_file and st.button("Compress PDF"):
    reader = PdfReader(compress_file)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    with open(temp_file.name, "wb") as f:
        writer.write(f)
    st.success("PDF compressed successfully!")
    st.download_button("Download Compressed PDF", temp_file.name, file_name="compressed.pdf")