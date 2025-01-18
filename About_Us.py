import streamlit as st
import numpy as np 
np_bool = bool(True)  # or np.bool_(True)

st.set_page_config(
    page_title='shrdc day4'
)


def main():
    st.title("Welcome to Group 3!")
    #st.image("group_photo.jpg", width=300)  # Replace with the actual path to your group photo

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Member 1: Adlina Anati")
        st.image("https://3.bp.blogspot.com/-uQr1gPf3ao4/WlvkCzgKjPI/AAAAAAABO04/8UnTNOOY_0kLYr8FVZQq17qwzQeXntzKgCKgBGAs/s1600/5a0c694f82e02d31ecb8d007.png",  width=100)
        st.write("**Contact:** adlinaanati@gmail.com")

    with col2:
        st.header("Member 2: Nurul Afiqah")
        st.image("https://th.bing.com/th/id/R.c30cc6b07acbb55ee010eb7413ad2b49?rik=%2bwS%2bnhWE8MUFJw&riu=http%3a%2f%2fvignette3.wikia.nocookie.net%2fdoblaje%2fimages%2f1%2f12%2fInside_Out_Sadness.png%2frevision%2flatest%3fcb%3d20160106014125%26path-prefix%3des&ehk=aXX%2fbXml8MSFUoFFksIEv0aA8IzkY%2b51jLvUM7TRzqs%3d&risl=&pid=ImgRaw&r=0", width=100)  # Replace with the actual path to Member 2's photo
        st.write("**Contact:** afiqah_zulkifle@outlook.com")

    with col3:
        st.header("Member 3: Anis Izzati")
        st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1ebd221d-3581-4775-8f4c-086c377bc4c3/dh21yyg-13113c8c-055f-4fb6-b152-7bdca2c20e26.png/v1/fill/w_1280,h_854/inside_out_2_envy_png_by_docbuffflash82_dh21yyg-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODU0IiwicGF0aCI6IlwvZlwvMWViZDIyMWQtMzU4MS00Nzc1LThmNGMtMDg2YzM3N2JjNGMzXC9kaDIxeXlnLTEzMTEzYzhjLTA1NWYtNGZiNi1iMTUyLTdiZGNhMmMyMGUyNi5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.-XGge6hqWTgTAZYiUUWARfJOiEe7JAbmXwlbLeL7PWo", width=200)  # Replace with the actual path to Member 1's photo
        st.write("**Contact:** anizizzati178@gmail.com")

   

if __name__ == "__main__":
    main()




