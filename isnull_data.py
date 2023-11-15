import streamlit as st
import pandas as pd

# Fungsi untuk mendeteksi nilai kosong
def detect_missing_values(file_path):
    df = pd.read_csv(file_path)
    missing_values = df.isnull().sum()
    return missing_values

# Halaman utama aplikasi Streamlit
def main():
    st.title("Aplikasi Mendeteksi Nilai Kosong dalam Data CSV")

    # Mengunggah file CSV
    uploaded_file = st.file_uploader("Unggah File CSV", type=["csv"])

    # Menampilkan informasi nilai kosong jika file diunggah
    if uploaded_file is not None:
        st.success("File CSV berhasil diunggah.")
        st.write("### Informasi Nilai Kosong:")
        missing_values_info = detect_missing_values(uploaded_file)
        st.write(missing_values_info)

if __name__ == "__main__":
    main()
