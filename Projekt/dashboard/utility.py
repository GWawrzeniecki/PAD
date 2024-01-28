import subprocess


def convert_to_markdown(notebook_path):
    # Convert the notebook to markdown
    subprocess.run(["jupyter", "nbconvert", "--to", "markdown", notebook_path])
