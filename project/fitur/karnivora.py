import streamlit as st

class HewanKarnivora:
    def __init__(self):
        self.daftar_karnivora = {
            "singa": {
                "ciri": (
                    "Singa adalah pemakan daging (karnivora). "
                    "Hewan ini dikenal sebagai raja hutan karena kekuatan dan keberaniannya."
                ),
                "makanan": "daging",
                "gambar": "images/singa.jpg"
            },
            "harimau": {
                "ciri": (
                    "Harimau adalah hewan soliter yang berburu mangsa di malam hari. "
                    "Ciri khasnya adalah garis-garis hitam pada tubuh oranye yang berfungsi sebagai kamuflase."
                ),
                "makanan": "daging",
                "gambar": "images/harimau.jpg"
            },
            "serigala": {
                "ciri": (
                    "Serigala adalah hewan sosial yang berburu dalam kawanan. "
                    "Mereka berkomunikasi melalui lolongan dan hidup di berbagai habitat."
                ),
                "makanan": "daging",
                "gambar": "images/serigala.jpg"
            },
            "cheetah": {
                "ciri": (
                    "Cheetah adalah pelari tercepat di dunia hewan. "
                    "Hewan ini berburu dengan kecepatan tinggi untuk menangkap mangsanya."
                ),
                "makanan": "daging",
                "gambar": "images/cheetah.jpg"
            },
            "macan tutul": {
                "ciri": (
                    "Macan tutul adalah kucing besar yang dapat memanjat pohon dengan mudah. "
                    "Hewan ini hidup di berbagai habitat, termasuk hutan dan savana."
                ),
                "makanan": "daging",
                "gambar": "images/macan_tutul.jpg"
            },
            "hyena": {
                "ciri": (
                    "Hyena adalah hewan pemakan bangkai yang juga berburu mangsa. "
                    "Hewan ini memiliki gigitan yang sangat kuat."
                ),
                "makanan": "daging",
                "gambar": "images/hyena.jpg"
            },
            "buaya": {
                "ciri": (
                    "Buaya adalah reptil besar yang hidup di air tawar dan payau. "
                    "Hewan ini memangsa ikan, burung, dan mamalia."
                ),
                "makanan": "daging",
                "gambar": "images/buaya.jpg"
            },
            "elang": {
                "ciri": (
                    "Elang adalah burung pemangsa dengan penglihatan tajam. "
                    "Hewan ini berburu mamalia kecil, burung, dan reptil."
                ),
                "makanan": "daging",
                "gambar": "images/elang.jpg"
            }
        }

    def tampilkan_ciri(self, nama):
        return self.daftar_karnivora.get(nama, None)

    def daftar_hewan(self):
        return self.daftar_karnivora.keys()


def main():
    st.title("Halaman Karnivora")
    st.subheader("Selamat datang di halaman Karnivora")

    karnivora = HewanKarnivora()

    nama_hewan = st.selectbox("Pilih nama hewan", options=["Pilih"] + list(karnivora.daftar_hewan()))
    makanan_hewan = st.selectbox("Pilih makanan hewan", options=["Pilih", "daging", "tumbuhan"])

    if st.button("Tampilkan Ciri"):
        if nama_hewan == "Pilih" or makanan_hewan == "Pilih":
            st.error("Silakan pilih nama hewan dan makanan.")
        else:
            data_hewan = karnivora.tampilkan_ciri(nama_hewan)
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
                st.error(f"Maaf, {nama_hewan.capitalize()} tidak ditemukan dalam daftar Karnivora.")

    if st.button("Tampilkan Semua Hewan Karnivora"):
        st.subheader("Daftar Hewan Karnivora")
        for hewan, info in karnivora.daftar_karnivora.items():
            st.markdown(f"### {hewan.capitalize()}")
            st.markdown(f"- **Ciri**: {info['ciri']}")
            st.markdown(f"- **Makanan**: {info['makanan']}")
            st.image(info["gambar"], caption=f"Gambar {hewan.capitalize()}")

if __name__ == "__main__":
    main()
