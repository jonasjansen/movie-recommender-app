import streamlit as st
from streamlit_star_rating import st_star_rating

st.set_page_config(
    page_title="Recommender by Genre",
    page_icon="🍿",
)

st.write("# Movie Recommendations by Genre")

st.write("---")

st.write("### Choose a Genre")

option = st.selectbox(
    "",
    ("Action", "Comedy", "Horror"),
    index=None,
    placeholder="Select you Genre...",
)

st.write("---")

st.write("### Your recommended movies")

# TODO: Show New Movies
