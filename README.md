# **Python Code Linter:**

Welcome to the Python Code Linter project! This tool is designed to help developers identify and correct common issues in Python code, such as improper indentation, overly long lines, and syntax errors. The linter ensures your code adheres to clean coding practices and can improve overall code quality.

---

## Features
- **Indentation Check**: Detects inconsistent use of tabs and spaces and missing indentation in blocks (e.g., `if`, `for`, `while`, function definitions).
- **Line Length Enforcement**: Flags lines that exceed the configurable maximum character limit (default: 80 characters).
- **Syntax Error Detection**: Identifies syntax errors in Python code for quick fixes.
- **Customizable Rules**: Allows users to specify the types of checks (e.g., long lines, indentation) for tailored analysis.
- **Multi-File Support**: Can analyze one or multiple files in a single run.

---

## Project Components
1. **`Indentation.py`**:
   - Contains a simple code snippet with improper indentation to test the linter's ability to detect and flag such issues.

2. **`Length.py`**:
   - Includes a function with a line exceeding the 80-character limit, designed to test line length checks.

3. **`SyntaxError.py`**:
   - Features a syntax error (missing closing parenthesis) for evaluating the linter's syntax analysis capabilities.

4. **`Linter.py`**:
   - The core of the project. Implements the PythonCodeLinter class, which reads files, performs line-by-line and AST-based checks, and generates a comprehensive report of code issues.

---

## Technologies Used
- **Python 3.x**
- **`ast` module**: For analyzing the Abstract Syntax Tree (AST) of Python code.
- **`os` module**: For file operations and path management.

---

## How to Use
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/python-code-linter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd python-code-linter
    ```
3. Run the linter on the sample files or specify your own:
    ```bash
    python Linter.py
    ```
    - By default, the script analyzes `SyntaxError.py`, `Indentation.py`, and `Length.py`.
    - To analyze additional files, specify them in the `files_to_analyze` list in `Linter.py`.

---

## Example Output
```plaintext
File: SyntaxError.py, Line: 3, Severity: High, Issue: SyntaxError: unexpected EOF while parsing
File: Indentation.py, Line: 2, Severity: Medium, Issue: Inconsistent indentation (mixing tabs and spaces)
File: Length.py, Line: 2, Severity: Low, Issue: Line exceeds 80 characters
