import streamlit as st
from transformers import pipeline

from src.inference import extract_information

# Define qa pipeline
qa_pipeline = pipeline("question-answering", model="andikazf15/IndoBERT-QA-product-pred")

# Streamlit app
st.title("AI untuk Ekstrak Informasi Pengiriman Barang")
st.write("Masukkan pesan/teks ke dalam kolom konteks")

# Input context and question
context = st.text_area("Konteks", "Saya mau memesan 10 piring, 20 gelas dengan motif batik ke Bandung")

# Perform QA inference
if st.button("Dapatkan Informasi"):
    if context:
        df = extract_information(qa_pipeline, context)
        st.table(df)
    else:
        st.write("Berikan konteks pada pada input yang disediakan")