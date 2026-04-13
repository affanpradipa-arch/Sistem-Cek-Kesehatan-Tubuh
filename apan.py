import streamlit as st

# Inisialisasi session state
if "data_mahasiswa" not in st.session_state:
    st.session_state.data_mahasiswa = []

st.title("📚 Sistem Data Mahasiswa Sederhana")

menu = st.sidebar.selectbox("Pilih Menu", ["Tambah Data", "Tampilkan Data", "Hapus Data"])

# ======================
# TAMBAH DATA
# ======================
if menu == "Tambah Data":
    st.subheader("Tambah Data Mahasiswa")

    nama = st.text_input("Nama")
    nim = st.text_input("NIM")
    jurusan = st.text_input("Jurusan")

    if st.button("Simpan"):
        if nama and nim and jurusan:
            st.session_state.data_mahasiswa.append({
                "nama": nama,
                "nim": nim,
                "jurusan": jurusan
            })
            st.success("Data berhasil ditambahkan!")
        else:
            st.warning("Semua field harus diisi!")

# ======================
# TAMPILKAN DATA
# ======================
elif menu == "Tampilkan Data":
    st.subheader("Daftar Mahasiswa")

    if st.session_state.data_mahasiswa:
        for i, mhs in enumerate(st.session_state.data_mahasiswa, start=1):
            st.write(f"{i}. {mhs['nama']} | {mhs['nim']} | {mhs['jurusan']}")
    else:
        st.info("Belum ada data.")

# ======================
# HAPUS DATA
# ======================
elif menu == "Hapus Data":
    st.subheader("Hapus Data Mahasiswa")

    if st.session_state.data_mahasiswa:
        pilihan = st.selectbox(
            "Pilih data yang ingin dihapus",
            range(len(st.session_state.data_mahasiswa)),
            format_func=lambda x: f"{st.session_state.data_mahasiswa[x]['nama']} ({st.session_state.data_mahasiswa[x]['nim']})"
        )

        if st.button("Hapus"):
            st.session_state.data_mahasiswa.pop(pilihan)
            st.success("Data berhasil dihapus!")
    else:
        st.info("Belum ada data.")
