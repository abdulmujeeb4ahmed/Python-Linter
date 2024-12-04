# Python Code Linter

This project is a static analysis tool designed to detect common Python code issues such as unused variables, improper indentation, long lines of code, and syntax errors. The linter helps ensure better code quality and maintainability.

## Features

### **Code Analysis**
- **Long Lines Detection**:
  - Identifies lines exceeding the specified character limit (default: 80).
- **Indentation Checks**:
  - Detects inconsistent indentation, such as mixing tabs and spaces.
  - Flags missing indentation in code blocks.
- **Syntax Error Detection**:
  - Captures and reports syntax errors in Python files.
 
### **Customizable Parameters**
- Allows setting a custom maximum line length for analysis.
- Enables selective checks for specific issues like `long_lines` or `indentation`.

### **Comprehensive Reporting**
- Summarizes identified issues, including the file name, line number, severity, and issue description.

---

## Files

### **Linter.py**
- Main Python script for static analysis, including features for analyzing long lines, indentation issues, and syntax errors.

### **SyntaxError.py**
- Test file containing a syntax error for validating the linter's error-detection capabilities.

### **Length.py**
- Test file with a line exceeding the maximum character limit to demonstrate long-lines detection.

### **Indentation.py**
- Test file with improper indentation to verify indentation error handling.

---

## Dependencies

This project requires the following Python libraries:
- **os**
- **ast**

These libraries are included in the Python standard library, so no additional installations are needed.

---

## Usage

### Clone the Repository
```bash
git clone https://github.com/yourusername/Python-Code-Linter.git
