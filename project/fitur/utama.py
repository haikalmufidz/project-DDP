import streamlit as st

class Hewan:
    def __init__(self, jenis, deskripsi, fakta, gambar, caption):
        self.jenis = jenis
        self.deskripsi = deskripsi
        self.fakta = fakta
        self.gambar = gambar
        self.caption = caption

    def tampilkan_info(self):
        st.header(f"🐾 {self.jenis}")
        col1, col2, col3 = st.columns(3)

        # Menampilkan gambar dengan caption
        for i, col in enumerate([col1, col2, col3]):
            if i < len(self.gambar):
                col.image(self.gambar[i], caption=self.caption[i], use_container_width=True)

        # Menampilkan deskripsi dan fakta
        st.write(self.deskripsi)
        st.write("**Fakta Unik:**")
        for fakta in self.fakta:
            st.write(f"- {fakta}")

# Membuat objek hewan untuk karnivora
karnivora = Hewan(
    jenis="Karnivora",
    deskripsi="""
        Karnivora adalah hewan yang bergantung pada daging sebagai sumber utama makanannya. Hewan ini memiliki gigi yang tajam
        dan cakar yang kuat untuk berburu dan memotong daging mangsanya. Karnivora sering kali merupakan predator di ekosistemnya.
        Contoh hewan karnivora meliputi singa, harimau, serigala, elang, dan buaya.
    """,
    fakta=[
        "Singa dikenal sebagai 'Raja Hutan' karena posisinya di puncak rantai makanan.",
        "Harimau adalah predator soliter yang sangat kuat.",
        "Serigala hidup dan berburu dalam kelompok untuk menangkap mangsa yang lebih besar.",
    ],
    gambar=["images/karnivora1.jpg", "images/karnivora2.jpg", "images/karnivora3.jpg"],
    caption=["Harimau", "SInga", "Serigala"],
)

# Membuat objek hewan untuk herbivora
herbivora = Hewan(
    jenis="Herbivora",
    deskripsi="""
        Herbivora adalah hewan yang makanannya berasal dari tumbuhan, seperti rumput, daun, buah, dan bunga. Hewan ini memainkan
        peran penting dalam menjaga keseimbangan ekosistem sebagai konsumen primer. Contoh hewan herbivora meliputi sapi, kambing, rusa, gajah, dan kuda.
    """,
    fakta=[
        "Gajah adalah mamalia darat terbesar yang hanya memakan tumbuhan.",
        "Sapi memiliki sistem pencernaan yang kompleks untuk mencerna serat.",
        "Rusa sering hidup dalam kawanan untuk melindungi diri dari predator.",
    ],
    gambar=["images/herbivora1.jpg", "images/herbivora2.jpg", "images/herbivora3.jpg"],
    caption=["Sapi", "Gajah", "Rusa"],
)

# Membuat objek hewan untuk omnivora
omnivora = Hewan(
    jenis="Omnivora",
    deskripsi="""
        Omnivora adalah hewan yang memakan daging dan tumbuhan. Mereka memiliki kemampuan untuk beradaptasi dengan berbagai 
        jenis makanan, sehingga memiliki keuntungan di lingkungan yang berubah-ubah. Contoh hewan omnivora meliputi ayam, beruang, babi, manusia, dan monyet.
    """,
    fakta=[
        "Beruang dapat bertahan hidup di hutan, padang rumput, dan pegunungan.",
        "Ayam juga memakan serangga kecil sebagai sumber protein.",
        "Babi adalah hewan yang mudah beradaptasi dengan berbagai jenis makanan.",
    ],
    gambar=["images/omnivora1.jpg", "images/omnivora2.jpg", "images/omnivora3.jpg"],
    caption=["Beruang", "Ayam", "Babi"],
)

def main():
    st.title("Penjelasan Hewan: Karnivora, Herbivora, dan Omnivora")
    st.markdown("---")

    # Menampilkan informasi untuk setiap jenis hewan
    karnivora.tampilkan_info()
    st.markdown("---")
    herbivora.tampilkan_info()
    st.markdown("---")
    omnivora.tampilkan_info()

    # Kesimpulan
    st.write("""
        **Kesimpulan:**
        - **Karnivora** adalah pemakan daging.
        - **Herbivora** adalah pemakan tumbuhan.
        - **Omnivora** adalah pemakan daging dan tumbuhan.

        Ketiga kelompok hewan ini memiliki peran penting dalam ekosistem, membantu menjaga keseimbangan rantai makanan.
    """)

if __name__ == "__main__":
    main()
