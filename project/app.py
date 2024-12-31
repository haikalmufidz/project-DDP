import streamlit as st
from fitur import utama, karnivora, herbivora, omnivora  # Import dari folder fitur

def main():
    st.sidebar.title("Navigasi")
    menu = st.sidebar.radio("Pilih Halaman", ["Utama", "Karnivora", "Herbivora", "Omnivora"])

    if menu == "Utama":
        utama.main()
    elif menu == "Karnivora":
        karnivora.main()
    elif menu == "Herbivora":
        herbivora.main()
    elif menu == "Omnivora":
        omnivora.main()

if __name__ == "__main__":
    main()
