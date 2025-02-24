import os
import json
import sys
import re
from nbformat import v4 as nbf

class LeetCodeHelper:
    """A class to generate LeetCode problem folders and Jupyter notebooks based on an input file."""

    def __init__(self, file_path, category=None):
        self.file_path = file_path
        self.title = None
        self.category = category  # If not specified, will be extracted from the input file
        self.code_template = None
        self.example_input = None
        self.method_name = "solve"  # Default method name if not detected

    def read_input_file(self):
        """Reads the input file and extracts the title, category (if not provided), code template, example input, and method name."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                content = f.read()

            lines = content.split("\n")

            # Extract problem title (first line)
            self.title = lines[0].strip()

            # Extract problem category from input (if not provided in command-line)
            if not self.category:
                category_match = re.search(r"Category:\s*(.*)", content)
                self.category = category_match.group(1).strip() if category_match else "Uncategorized"

            # Extract code template
            code_start = content.find("class Solution(object):")
            if code_start == -1:
                raise ValueError("❌ No valid Python class found in the input file.")

            self.code_template = content[code_start:].strip()

            # Extract method name dynamically
            method_match = re.search(r"def (\w+)\(self,", content)
            if method_match:
                self.method_name = method_match.group(1)

            # Extract Example 1 input (supports multiple variable names)
            example_match = re.search(r"Example 1:\s+Input:\s*(.*)", content)
            self.example_input = example_match.group(1).strip() if example_match else "[]"

        except FileNotFoundError:
            print(f"❌ Error: File '{self.file_path}' not found.")
            sys.exit(1)
        except ValueError as e:
            print(e)
            sys.exit(1)

    def get_problem_directory(self):
        """Parses the title and determines the appropriate problem directory."""
        if not self.title:
            print("❌ Error: No problem title found.")
            sys.exit(1)

        parts = self.title.split(". ", 1)
        if len(parts) < 2:
            print("❌ Invalid title format. Expected format: '238. Product of Array Except Self'")
            sys.exit(1)

        number, name = parts
        return os.path.join(self.category, f"{number}. {name}")

    def create_notebook(self, folder_path):
        """Generates a Jupyter Notebook with the extracted code template."""
        nb = nbf.new_notebook()
        complete_code = f"""{self.code_template}

solution = Solution()
solution.{self.method_name}({self.example_input})
"""

        nb.cells.append(nbf.new_code_cell(complete_code))

        notebook_path = os.path.join(folder_path, "code.ipynb")
        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=2)

        print(f"✅ Notebook created: {notebook_path}")

    def generate_folder_and_notebook(self):
        """Creates the problem folder and generates the Jupyter notebook inside it."""
        self.read_input_file()
        folder_path = self.get_problem_directory()

        # Ensure directory exists
        os.makedirs(folder_path, exist_ok=True)
        print(f"📂 Directory created: {folder_path}")

        # Generate the Jupyter notebook
        self.create_notebook(folder_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python helper.py <input_file> [category]")
        sys.exit(1)

    input_file = sys.argv[1]
    category = sys.argv[2] if len(sys.argv) > 2 else None  # Optional category

    helper = LeetCodeHelper(input_file, category)
    helper.generate_folder_and_notebook()