# Modifying Import Statements Using AST

## About the Project

This project aims to automate the modification of import statements in multiple Python projects that share common utility files. Often, when deploying individual projects, it's preferable to include utility files within each project rather than sharing a common utility folder. This tool facilitates this process by modifying import statements to reference utility files within the project itself.

The tool is implemented using the Abstract Syntax Tree (AST) module in Python, along with the `os` and `shutil` modules for file manipulation.

## How It Works

The tool traverses through the Python source files of each project and identifies import statements using the AST module. It then modifies import statements that reference utility files from a shared folder to instead reference utility files present within the project itself. This ensures that each project maintains its own copy of utility files and does not rely on a shared folder during deployment.

Here's a brief overview of how the tool works:

```python
import os
import shutil
import ast

# Define function to process each Python file
def process_file(path: str, filename: str) -> tuple:
    # Implement processing logic here...

# Iterate over files in the directory and process each Python file
for root, dirs, files in os.walk("./"):
    for filename in files:
        if not root.startswith("./proj"):
            continue
        is_error, result = process_file(root, filename)
        if is_error:
            print(f"ERROR: {result}")
            break
        else:
            print(f"RESULT: {os.path.join(root, filename)} - {result}")

```

## How to Use

1. **Clone the Repository**: Clone or download this repository to your local machine.
2. **Folder Structure**: Ensure your project folder structure follows the layout described below:
   ```
   root
   ├── proj1
   │   └── main.py
   ├── proj2
   │   └── main.py
   ├── projN
   │   └── main.py
   ├── utility
   │   ├── file1.py
   │   └── file2.py
   ├── build.ipynb
   └── Working with AST.py
   ```
3. **Run the Script**: Navigate to the root folder where all the projects are located. Run the `build.ipynb` Jupyter notebook or the `Working with AST.py` Python script.
4. **View Results**: After execution, check the modified Python source files in each project folder to verify that the import statements have been updated correctly.


