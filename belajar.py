import streamlit as st
import pandas as pd
import base64

st.title('Input Data')

if 'csv_created' not in st.session_state:
    st.session_state.csv_created = False

nama = st.text_input('Masukkan Nama:')
usia = st.number_input('Masukkan Usia:', min_value=0)

if st.button('Simpan'):
    if nama and usia:
        data = {'Nama': [nama], 'Usia': [usia]}
        df = pd.DataFrame(data)
        # Mode 'a' (append) untuk menambahkan data ke file CSV
        df.to_csv('data_input.csv', mode='a', index=False, header=not st.session_state.csv_created)
        st.session_state.csv_created = True
        st.success('Data berhasil disimpan ke file CSV.')
    else:
        st.warning('Mohon lengkapi semua field sebelum menyimpan.')

# Menambahkan fitur unduhan data
if st.session_state.csv_created:
    # Membaca data dari file CSV yang telah disimpan
    data = pd.read_csv('data_input.csv')

    # Fungsi untuk membuat tautan unduhan
    def download_csv(data):
        csv_file = data.to_csv(index=False)
        b64 = base64.b64encode(csv_file.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="data_input.csv">Unduh File CSV</a>'
        return href

    st.markdown(download_csv(data), unsafe_allow_html=True)
