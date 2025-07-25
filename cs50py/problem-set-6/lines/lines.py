import sys
import os

def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = 0
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                line_count += 1
        return line_count

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Too few or too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the provided file has a .py extension
    if not filename.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)

    # Check if the specified file exists
    if not os.path.exists(filename):
        print("File does not exist")
        sys.exit(1)

    # Count lines of code excluding comments and blank lines
    lines_count = count_lines(filename)

    # Output the total count of lines
    print(f"Total lines of code in '{filename}': {lines_count}")
