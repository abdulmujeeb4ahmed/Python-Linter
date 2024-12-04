import ast
import os

class PythonCodeLinter:
    def __init__(self, files, max_line_length=80, classifications=None):
        self.files = files if isinstance(files, list) else [files]
        self.max_line_length = max_line_length
        self.classifications = classifications if classifications else ['long_lines', 'indentation']
        self.issues = []

    def analyze_code(self):
        for file_path in self.files:
            file_name = os.path.basename(file_path)
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
            except FileNotFoundError:
                print(f"Error: The file '{file_name}' does not exist.")
                continue

            file_issues = []

            # Perform line-based checks
            for line_number, line in enumerate(lines, start=1):
                if 'long_lines' in self.classifications:
                    self.check_long_lines(line, line_number, file_name, file_issues)
                if 'indentation' in self.classifications:
                    self.check_indentation(line, line_number, file_name, file_issues)

            # Perform syntax and AST-based checks
            try:
                tree = ast.parse(''.join(lines))
                if 'indentation' in self.classifications:
                    self.check_missing_indentation(tree, lines, file_name, file_issues)
            except SyntaxError as e:
                # Capture syntax errors
                file_issues.append({
                    'filename': file_name,
                    'line': e.lineno,
                    'issue': f"SyntaxError: {e.msg}",
                    'severity': 'High'
                })

            self.issues.extend(file_issues)

    def check_long_lines(self, line, line_number, file_name, file_issues):
        if len(line) > self.max_line_length:
            file_issues.append({
                'filename': file_name,
                'line': line_number,
                'issue': f"Line exceeds {self.max_line_length} characters",
                'severity': 'Low'
            })

    def check_indentation(self, line, line_number, file_name, file_issues):
        leading_whitespace = line[:len(line) - len(line.lstrip())]
        if '\t' in leading_whitespace and ' ' in leading_whitespace:
            file_issues.append({
                'filename': file_name,
                'line': line_number,
                'issue': "Inconsistent indentation (mixing tabs and spaces)",
                'severity': 'Medium'
            })

    def check_missing_indentation(self, tree, lines, file_name, file_issues):
        """
        Detect missing indentation for blocks like `if`, `else`, `for`, `while`, and function definitions.
        """
        class IndentationVisitor(ast.NodeVisitor):
            def __init__(self):
                self.indentation_errors = []

            def visit_FunctionDef(self, node):
                self.check_block_indentation(node, lines)
                self.generic_visit(node)

            def visit_If(self, node):
                self.check_block_indentation(node, lines)
                self.generic_visit(node)

            def visit_For(self, node):
                self.check_block_indentation(node, lines)
                self.generic_visit(node)

            def visit_While(self, node):
                self.check_block_indentation(node, lines)
                self.generic_visit(node)

            def visit_With(self, node):
                self.check_block_indentation(node, lines)
                self.generic_visit(node)

            def check_block_indentation(self, node, lines):
                """
                Checks if a block has proper indentation.
                """
                start_line = node.lineno - 1  # AST lineno starts at 1; Python lists are 0-based
                if start_line + 1 >= len(lines):
                    return  # Avoid IndexError if no lines follow

                next_line = lines[start_line + 1].strip()
                current_indentation = len(lines[start_line]) - len(lines[start_line].lstrip())

                # Ensure the next line belongs to the block and is indented more
                if next_line and not next_line.startswith('#'):  # Skip comments
                    next_indentation = len(lines[start_line + 1]) - len(lines[start_line + 1].lstrip())
                    if next_indentation <= current_indentation:
                        self.indentation_errors.append({
                            'line': start_line + 2,  # Adjust for 1-based line number
                            'issue': "Missing indentation for code block"
                        })

        visitor = IndentationVisitor()
        visitor.visit(tree)

        for error in visitor.indentation_errors:
            file_issues.append({
                'filename': file_name,
                'line': error['line'],
                'issue': error['issue'],
                'severity': 'Medium'
            })

    def generate_report(self):
        if not self.issues:
            print("No issues found.")
        else:
            for issue in self.issues:
                print(f"File: {issue['filename']}, Line: {issue['line']}, Severity: {issue['severity']}, Issue: {issue['issue']}")

# Example Usage
if __name__ == "__main__":
    # Specify the file(s) to analyze directly
    files_to_analyze = ['SyntaxError.py', 'Indentation.py', 'Length.py']
    linter = PythonCodeLinter(
        files=files_to_analyze,
        max_line_length=80,  # Set your desired maximum line length
        classifications=['long_lines', 'indentation']  # Specify checks
    )
    linter.analyze_code()
    linter.generate_report()
