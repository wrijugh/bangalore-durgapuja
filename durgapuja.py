import streamlit as st
import pandas as pd
import io

def make_clickable(val):
    return f'<a target="_blank" href="{val}">Map</a>'

# Set the page title
st.title("Bangalore Durga Puja")
st.set_page_config(
    page_title="Bangalore Durga Puja"
)

# st.("Bangalore Durga Puja")
FILE_PATH = 'DurgaPuja2025v1.csv'
df = pd.read_csv(FILE_PATH)

# --- Search Bar ---
# Use st.text_input to capture the user's search query
search_term = st.text_input(
    "Enter a search term (Name or Location):", 
    value="",
    placeholder="e.g., HSR or East"
).lower() # Convert to lowercase for case-insensitive search

# --- Filtering Logic ---
if search_term:
    # Create a mask to filter the DataFrame
    # Check if the search term is in EITHER the 'Name' or 'City' column
    mask = df.apply(lambda row: 
        search_term in str(row['Area']).lower() or 
        search_term in str(row['Puja Name']).lower() or 
        search_term in str(row['Location']).lower() or 
        search_term in str(row['Committee Name']).lower(), 
        axis=1
    )
    
    # Apply the mask to get the filtered DataFrame
    filtered_df = df[mask]
    
    st.subheader(f"Results for '{search_term}' ({len(filtered_df)} found)")

    
    # Apply the function to the 'GPS Location' column
    df_html_links = df.copy()
    df_html_links['GPS Location'] = df_html_links['GPS Location'].apply(make_clickable)

    # Convert the entire DataFrame to HTML, but disable the header escaping
    # so the <a> tags are rendered as HTML.

    html_table = df_html_links.to_html(escape=False, index=False)
    st.markdown(html_table, unsafe_allow_html=True)

           
else:
    # Display the full DataFrame if no search term is entered
    st.subheader("Durga Puja Full List")
    # st.dataframe(df, use_container_width=True)
    # Apply the function to the 'GPS Location' column
    df_html_links = df.copy()
    df_html_links['GPS Location'] = df_html_links['GPS Location'].apply(make_clickable)
    html_full = df_html_links.to_html(escape=False, index=False)
    st.markdown(html_full, unsafe_allow_html=True)


st.write("https://github.com/wrijugh/bangalore-durgapuja")