import streamlit as st

class HewanHerbivora:
    def __init__(self):
        self.daftar_herbivora = {
            "kuda": {
                "ciri": (
                    "Kuda adalah hewan pelari cepat dengan tubuh yang kuat. "
                    "Hewan ini memakan rumput dan tanaman hijau lainnya."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/kuda.jpg"
            },
            "gajah": {
                "ciri": (
                    "Gajah adalah mamalia darat terbesar dengan belalai yang kuat. "
                    "Hewan ini memakan dedaunan, buah, dan kulit kayu."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/gajah.jpg"
            },
            "kambing": {
                "ciri": (
                    "Kambing adalah hewan pemakan tumbuhan yang suka memanjat. "
                    "Hewan ini sering ditemukan di peternakan."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/kambing.jpg"
            },
            "rusa": {
                "ciri": (
                    "Rusa adalah hewan dengan tanduk indah yang hidup di padang rumput dan hutan. "
                    "Hewan ini memakan rumput dan dedaunan."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/rusa.jpg"
            },
            "zebra": {
                "ciri": (
                    "Zebra adalah hewan yang memiliki pola garis hitam putih pada tubuhnya. "
                    "Hewan ini hidup di savana dan memakan rumput."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/zebra.jpg"
            },
            "koala": {
                "ciri": (
                    "Koala adalah marsupial pemakan daun eukaliptus. "
                    "Hewan ini dikenal karena hidup di pohon."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/koala.jpg"
            },
            "badak": {
                "ciri": (
                    "Badak adalah hewan besar dengan cula di hidungnya. "
                    "Hewan ini memakan rumput dan dedaunan."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/badak.jpg"
            },
            "unta": {
                "ciri": (
                    "Unta adalah hewan gurun dengan punuk di punggungnya. "
                    "Hewan ini memakan tumbuhan gurun dan dapat bertahan tanpa air."
                ),
                "makanan": "tumbuhan",
                "gambar": "images/unta.jpg"
            }
        }

    def tampilkan_ciri(self, nama):
        return self.daftar_herbivora.get(nama, None)

    def daftar_hewan(self):
        return self.daftar_herbivora.keys()


def main():
    st.title("Halaman Herbivora")
    st.subheader("Selamat datang di halaman Herbivora")

    herbivora = HewanHerbivora()

    nama_hewan = st.selectbox("Pilih nama hewan", options=["Pilih"] + list(herbivora.daftar_hewan()))
    makanan_hewan = st.selectbox("Pilih makanan hewan", options=["Pilih", "daging", "tumbuhan"])

    if st.button("Tampilkan Ciri"):
        if nama_hewan == "Pilih" or makanan_hewan == "Pilih":
            st.error("Silakan pilih nama hewan dan makanan.")
        else:
            data_hewan = herbivora.tampilkan_ciri(nama_hewan)
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
                st.error(f"Maaf, {nama_hewan.capitalize()} tidak ditemukan dalam daftar Herbivora.")

    if st.button("Tampilkan Semua Hewan Herbivora"):
        st.subheader("Daftar Hewan Herbivora")
        for hewan, info in herbivora.daftar_herbivora.items():
            st.markdown(f"### {hewan.capitalize()}")
            st.markdown(f"- **Ciri**: {info['ciri']}")
            st.markdown(f"- **Makanan**: {info['makanan']}")
            st.image(info["gambar"], caption=f"Gambar {hewan.capitalize()}")

if __name__ == "__main__":
    main()
