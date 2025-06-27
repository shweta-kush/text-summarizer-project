import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


Project_name ="TextSummarizer"
list_of_files= {
    ".github.com/workflows/.gitkeep",
    "src/{Project_name}/__init__.py",
    "src/{Project_name}/components/__init__.py",
    "src/{Project_name}/utils/__init__.py",
    "src/{Project_name}/utils/common.py",
    "src/{Project_name}/logging/__init__.py",
    "src/{Project_name}/config/__init__.py",
    "src/{Project_name}/config/configuration.py",
    "src/{Project_name}/pipline/__init__.py",
    "src/{Project_name}/entity/__init__.py",
    "src/{Project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    "README.md",
    "setup.py",
    "research/trials.py",
    # "tests/test_project_name.py"

}

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            # file.write("# " + filename)
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File: {filepath} already exists.")




