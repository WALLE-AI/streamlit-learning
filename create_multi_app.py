import streamlit as st


def creare_nav():
    create_page = st.Page("pages/file_upload.py", title="文件上传", icon=":material/add_circle:")
    delete_page = st.Page("pages/delete.py", title="Delete entry", icon=":material/delete:")

    pg = st.navigation([create_page, delete_page])
    st.set_page_config(page_title="Data manager", page_icon="images/pdf.png")
    pg.run()


