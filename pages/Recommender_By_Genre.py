import streamlit as st

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

# TODO: Remove. Only for debugging.
#st.write("You selected:", option)

st.write("---")

st.write("### Your recommended movies")

# TODO: Build a List of moves based on the selected genre.
