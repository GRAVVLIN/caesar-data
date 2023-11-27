import streamlit as st
import pandas as pd

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
