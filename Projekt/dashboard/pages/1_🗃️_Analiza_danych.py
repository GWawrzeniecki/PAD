import streamlit as st
import subprocess


# nie mogłem zaimportować utility-path errors
def convert_to_markdown(notebook_path):
    # Convert the notebook to markdown
    subprocess.run(["jupyter", "nbconvert", "--to", "markdown", notebook_path])


st.markdown("# Analiza i czyszczenie zbioru danych")

convert_to_markdown("Projekt/data_prepare.ipynb")

with open("Projekt/data_prepare.md", "r", encoding="utf-8") as f:
    markdown_content = f.read()
st.markdown(markdown_content, unsafe_allow_html=True)
