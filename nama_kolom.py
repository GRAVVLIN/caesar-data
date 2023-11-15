import pandas as pd
import streamlit as st

# Fungsi untuk melihat nama kolom
def view_column_names(file_path):
    df = pd.read_csv(file_path)
    return df.columns.tolist()

# Halaman utama aplikasi Streamlit
def main():
    st.title("Aplikasi Melihat Nama Kolom Data CSV")

    # Mengunggah file CSV
    uploaded_file = st.file_uploader("Unggah File CSV", type=["csv"])

    # Menampilkan nama kolom jika file diunggah
    if uploaded_file is not None:
        st.success("File CSV berhasil diunggah.")
        st.write("### Nama-nama Kolom:")
        column_names = view_column_names(uploaded_file)
        st.write(column_names)

if __name__ == "__main__":
    main()