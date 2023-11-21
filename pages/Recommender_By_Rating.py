import streamlit as st
from streamlit_star_rating import st_star_rating

st.set_page_config(
    page_title="Recommender by Rating",
    page_icon="⭐",
)


st.write("# Movie Recommendations by Genre")

st.write("---")

st.write("### Rate as many movies as possible")

with st.container():
    # Create a list to store the ratings for each component
    ratings_list = [[0] * 5 for _ in range(20)]

    # Loop through each row in the grid
    for i in range(20):
        # Create a row with 5 columns
        components = st.columns(5)

        # Loop through each column in the row
        for j in range(5):
            # Display a component in the column
            with components[j]:
                # Display a title for the component (you can customize this)
                st.write(f"Component {i + 1}-{j + 1}")

                # Display your custom star rating component and update the ratings_list
                #st_star_rating(label="Please rate you experience", size=20, maxValue=5, defaultValue=0, key="rating", dark_theme=True)
                ratings_list[i][j] = st_star_rating(
                    f"Rating-{i + 1}-{j + 1}", size=15, maxValue=5,
                    defaultValue=ratings_list[i][j], key=f"{i}-{j}", dark_theme=True)

# TODO: Add proceed button
# TODO: Show New Movies