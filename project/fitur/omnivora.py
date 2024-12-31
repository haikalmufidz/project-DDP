import streamlit as st

class HewanOmnivora:
    def __init__(self):
        self.daftar_omnivora = {
            "beruang": {
                "ciri": (
                    "Beruang adalah hewan besar dengan cakar yang kuat. "
                    "Hewan ini memakan buah-buahan, ikan, dan mamalia kecil."
                ),
                "makanan": "tumbuhan dan daging",
                "gambar": "images/beruang.jpg"
            },
            "babi": {
                "ciri": (
                    "Babi adalah hewan dengan tubuh gemuk yang hidup di peternakan. "
                    "Hewan ini memakan berbagai macam makanan, termasuk sisa makanan."
                ),
                "makanan": "tumbuhan dan daging",
                "gambar": "images/babi.jpg"
            },
            "rubah": {
                "ciri": (
                    "Rubah adalah hewan pintar dan gesit. "
                    "Hewan ini memakan buah, serangga, dan hewan kecil."
                ),
                "makanan": "tumbuhan dan daging",
                "gambar": "images/rubah.jpg" 
            },
            "ayam": {
                "ciri": (
                    "Ayam adalah unggas yang hidup di daratan. "
                    "Hewan ini memakan biji-bijian, serangga, dan sisa makanan."
                ),
                "makanan": "tumbuhan dan daging",
                "gambar": "images/ayam.jpg"
            },
            
            "tikus": {
                "ciri": (
                    "Tikus adalah hewan pengerat yang hidup di berbagai tempat. "
                    "Hewan ini memakan biji-bijian, buah, dan sisa makanan."
                ),
                "makanan": "tumbuhan dan daging",
                "gambar": "images/tikus.jpg"
            },
            "orangutan": {
                "ciri": (
                    "Orangutan adalah primata besar yang hidup di hutan tropis. "
                    "Hewan ini memakan buah-buahan, daun, dan serangga."
                ),
                "makanan": "tumbuhan dan daging",
                "gambar": "images/orangutan.jpg"
            },
            "kasuari": {
                "ciri": (
                    "Kasuari adalah burung besar yang tidak bisa terbang. "
                    "Hewan ini memakan buah-buahan, serangga, dan biji-bijian."
                ),
                "makanan": "tumbuhan dan daging",
                "gambar": "images/kasuari.jpg"
            }
        }

    def tampilkan_ciri(self, nama):
        return self.daftar_omnivora.get(nama, None)

    def daftar_hewan(self):
        return self.daftar_omnivora.keys()


def main():
    st.title("Halaman Omnivora")
    st.subheader("Selamat datang di halaman Omnivora")

    omnivora = HewanOmnivora()

    nama_hewan = st.selectbox("Pilih nama hewan", options=["Pilih"] + list(omnivora.daftar_hewan()))
    makanan_hewan = st.selectbox("Pilih makanan hewan", options=["Pilih", "daging", "tumbuhan", "tumbuhan dan daging"])

    if st.button("Tampilkan Ciri"):
        if nama_hewan == "Pilih" or makanan_hewan == "Pilih":
            st.error("Silakan pilih nama hewan dan makanan.")
        else:
            data_hewan = omnivora.tampilkan_ciri(nama_hewan)
            if data_hewan:
                if makanan_hewan == data_hewan["makanan"]:
                    hasil = [
                        f"Nama Hewan: {nama_hewan.capitalize()}",
                        f"Ciri Khas: {data_hewan['ciri']}",
                        f"Makanan Favorit: {makanan_hewan.capitalize()}"
                    ]
                    for item in hasil:
                        st.markdown(f"- **{item}**")

                    st.image(data_hewan["gambar"], caption=f"Gambar {nama_hewan.capitalize()}")
                else:
                    st.error(f"Error: {nama_hewan.capitalize()} tidak makan {makanan_hewan.capitalize()}. Hewan ini hanya makan {data_hewan['makanan']}.")
            else:
                st.error(f"Maaf, {nama_hewan.capitalize()} tidak ditemukan dalam daftar Omnivora.")

    if st.button("Tampilkan Semua Hewan Omnivora"):
        st.subheader("Daftar Hewan Omnivora")
        for hewan, info in omnivora.daftar_omnivora.items():
            st.markdown(f"### {hewan.capitalize()}")
            st.markdown(f"- **Ciri**: {info['ciri']}")
            st.markdown(f"- **Makanan**: {info['makanan']}")
            st.image(info["gambar"], caption=f"Gambar {hewan.capitalize()}")

if __name__ == "__main__":
    main()
