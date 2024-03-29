import os
import shutil
import ast

READ_MODE = "r"
WRITE_MODE = "w"


def process_file(path: str, filename: str) -> tuple:
    """
    Process the given Python source file in the specified path.

    Args:
        path (str): The path where the source file is located.
        filename (str): The name of the source file to process.

    Returns:
        tuple: A tuple indicating whether the process was successful (bool) and a message (str).
    """
    try:
        # Read the content of the source file
        with open(os.path.join(path, filename), READ_MODE) as file:
            source_code = file.read()

        # Parse the source code into an AST
        ast_tree = ast.parse(source_code)

        # Traverse the AST and modify import statements
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.ImportFrom):
                if node.level > 1:
                    # Extract the folder containing the shared module
                    shared_module_folder = (
                        node.module.split(".")[-2]
                        if len(node.module.split(".")) > 1
                        else ""
                    )

                    # Create the folder if it doesn't exist
                    shared_module_path = os.path.join(path, shared_module_folder)
                    if not os.path.exists(shared_module_path):
                        os.mkdir(shared_module_path)

                    # Copy the shared module file to the shared module folder
                    module_filename = node.module.split(".")[-1] + ".py"
                    destination_file_path = os.path.join(
                        shared_module_path, module_filename
                    )
                    shutil.copyfile(
                        node.module.replace(".", os.sep) + ".py", destination_file_path
                    )

                    # Update the import level to 1
                    node.level = 1

        # Generate modified source code from the modified AST
        modified_source_code = ast.unparse(ast_tree)

        # Write the modified source code back to the file
        with open(os.path.join(path, filename), WRITE_MODE) as file:
            file.write(modified_source_code)

    except Exception as e:
        # Return error message if an exception occurs
        return (True, str(e))

    # Return success message if the process completes without errors
    return (False, "Successfully completed!")


def main():
    """
    Main function to iterate over files in the directory and process each Python file.
    """
    # Iterate over files in the directory and process each Python file
    is_error = False
    for root, dirs, files in os.walk("./"):
        if is_error:
            break
        for filename in files:
            # Skip files not under the 'proj' directory
            if not root.startswith("./proj"):
                continue

            # Process the file and print the result
            is_error, result = process_file(root, filename)
            if is_error:
                print(f"ERROR: {result}")
                break
            else:
                print(f"RESULT: {os.path.join(root, filename)} - {result}")


# Check if the script is executed as the main module

if __name__ == "__main__":
    main()


# %%
