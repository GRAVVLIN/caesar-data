import streamlit as st
import pandas as pd
import base64

def display_home():
    st.title('INAUGURAKOM 2023')
    st.write('Makna Dan Filosofi Bahtera Nawasena Adalah, BAHTERA NAWASENA diambil dari bahasa sansekerta BAHTERA diartikan sebagai sebuah wadah yg bergerak dalam koordinasi, komunikasi, dan dapat bersinergi')
    st.image('INAU_PICS.png', caption='Logo INAUGURAKOM 2023', use_column_width=True)
    # Add content for home page here

def display_data_input():
    st.title('Daftar Hadir Tamu INAUURAKOM 2023')
    if 'csv_created' not in st.session_state:
        st.session_state.csv_created = False

    nama = st.text_input('Masukkan Nama:')
    angkatan = st.number_input('Masukan Tahun Angkatan Kamu', min_value=1996, max_value=2022)

    if st.button('Simpan'):
        if nama and angkatan:
            data = {'Nama': [nama], 'Usia': [angkatan]}
            df = pd.DataFrame(data)
            df.to_csv('data_input.csv', mode='a', index=False, header=not st.session_state.csv_created)
            st.session_state.csv_created = True
            st.success('Data Kehadiran Kamu Berhasil Disimpan!')
        else:
            st.warning('Silahkan Lengkapi Data Kamu Dengan Benar!')

def display_download():
    st.title('Download Data Peserta Hadir di Sini')
    if st.session_state.csv_created:
        data = pd.read_csv('data_input.csv')
        password = st.text_input('IF YOU WANT THE PERMISSION PLEASE CONTACT ADMIN, THANKS!!😊 ', type='password')

        if password == 'INAUKOM2023':
            def download_csv(data):
                csv_file = data.to_csv(index=False)
                b64 = base64.b64encode(csv_file.encode()).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="data_input.csv">Unduh File CSV</a>'
                return href

            st.markdown(download_csv(data), unsafe_allow_html=True)
        elif password != '':
            st.warning('UPSS YOUR PASSWORD INCORECT!!😊')

nav_selection = st.sidebar.radio("Bahtera Navigation", ["ABOUT US AND PHILOPHY LOGO!!", "ADD YOUR PRESSENCE HERE!!", "ATTENDANCE LIST DATA"])

if nav_selection == "ABOUT US AND PHILOPHY LOGO!!":
    display_home()
elif nav_selection == "ADD YOUR PRESSENCE HERE!!":
    display_data_input()
elif nav_selection == "ATTENDANCE LIST DATA":
    display_download()
