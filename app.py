import streamlit as st
import search_page
import visualization_page

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page:", ["Search Analytics", "Channel & Video Stats"])

if page == "Search Analytics":
    search_page.app()
else:
    visualization_page.app()