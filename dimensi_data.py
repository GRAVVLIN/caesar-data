import streamlit as st
import pandas as pd

# Fungsi untuk melihat dimensi DataFrame
def view_dimensions(file_path):
    df = pd.read_csv(file_path)
    jumlah_baris, jumlah_kolom = df.shape
    return jumlah_baris, jumlah_kolom

# Halaman utama aplikasi Streamlit
def main():
    st.title("Aplikasi Melihat Dimensi Data CSV")

    # Mengunggah file CSV
    uploaded_file = st.file_uploader("Unggah File CSV", type=["csv"])

    # Menampilkan dimensi jika file diunggah
    if uploaded_file is not None:
        st.success("File CSV berhasil diunggah.")
        st.write("Dimensi Data CSV:")
        jumlah_baris, jumlah_kolom = view_dimensions(uploaded_file)
        st.write(f"Jumlah Baris: {jumlah_baris}")
        st.write(f"Jumlah Kolom: {jumlah_kolom}")

if __name__ == "__main__":
    main()


