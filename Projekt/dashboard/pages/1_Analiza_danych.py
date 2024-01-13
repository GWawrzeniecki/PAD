import streamlit as st
import nbformat
from nbconvert import HTMLExporter
import subprocess

#
# def display_notebook(path):
#     with open(path) as f:
#         nb = nbformat.reads(f.read(), as_version=4)
#     exporter = HTMLExporter()
#     body, _ = exporter.from_notebook_node(nb)
#     st.components.v1.html(body, height=7500)
#
# st.markdown("# Analiza i czyszczenie zbioru danych")
#
# display_notebook("data_prepare.ipynb")

def convert_and_display_notebook(notebook_path):
    # Convert the notebook to markdown
    md_path = notebook_path.replace(".ipynb", ".md")
    subprocess.run(["jupyter", "nbconvert", "--to", "markdown", notebook_path])

    # Display the markdown in Streamlit
    with open(md_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
    st.markdown(markdown_content, unsafe_allow_html=True)

convert_and_display_notebook("data_prepare.ipynb")
