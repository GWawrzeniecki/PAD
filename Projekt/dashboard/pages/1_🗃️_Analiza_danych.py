import streamlit as st
import subprocess

def convert_and_display_notebook(notebook_path):
    # Convert the notebook to markdown
    md_path = notebook_path.replace(".ipynb", ".md")
    subprocess.run(["jupyter", "nbconvert", "--to", "markdown", notebook_path])

    # Display the markdown in Streamlit
    with open(md_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    st.markdown(markdown_content, unsafe_allow_html=True)

st.markdown("# Analiza i czyszczenie zbioru danych")

# convert_and_display_notebook("Projekt/data_prepare.ipynb")

with open("Projekt/data_prepare.ipynb", "r", encoding="utf-8") as f:
    markdown_content = f.read()
st.markdown(markdown_content, unsafe_allow_html=True)