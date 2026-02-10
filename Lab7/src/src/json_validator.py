"""
JSON Structure Validator — Lab 7

Validates the structural nesting of a JSON string using a Stack.
Reports the location (line, column) of any errors found.
"""

from stack import Stack


# Maps each closing character to its expected opening character.
MATCHING = {
    "}": "{",
    "]": "[",
}


def validate(json_string):
    stack = Stack()
    line , col = 1, 0
    errors = []
    in_string = False
    i = 0  

    while i < len(json_string):
        char = json_string[i]
        col += 1 
        if char == "\n":  
            line += 1
            col = 0
            i += 1
            continue 

        if char == '"' and not in_string:
            in_string = True
            i += 1
            continue

        if in_string:
            if char == '\\':
                i += 2
                col += 1
                continue
            elif char == '"':
                in_string = False
            i += 1
            continue

        if char in "{[":
            stack.push((char, line, col))
        elif char in "}]":
            if stack.is_empty():
                return False, [f"ERROR Line {line}, Col {col}: Unexpected '{char}'"]

            open_char, open_line, open_col = stack.pop()
            if MATCHING[char] != open_char:
                expected = next(k for k, v in MATCHING.items() if v == open_char)
                return False, [
                    f"ERROR Line {line}, Col {col}: Expected '{expected}' but found '{char}' "
                    f"(opening '{open_char}' at Line {open_line}, Col {open_col})"
                ]
        i += 1

    if in_string:
        return False, [
            f"ERROR Line {line}, Col {col}: Unterminated string"]

    if not stack.is_empty():
        errors = []
        while not stack.is_empty():
            open_char, open_line, open_col = stack.pop()
            errors.append(f"ERROR: Unclosed '{open_char}' at Line {open_line}, Col {open_col}")
        return False, errors
        
    return True, []



    """
    Validate the structural nesting of a JSON string.

    Checks that every { has a matching }, every [ has a matching ],
    and that quoted strings are properly closed.

    Args:
        json_string (str): The JSON text to validate.

    Returns:
        tuple: (is_valid, errors)
            - is_valid (bool): True if the structure is valid.
            - errors (list[str]): List of error message strings.
              Empty if valid.
    """



def validate_file(filepath):
    """
    Validate a JSON file by reading it and calling validate().

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        tuple: (is_valid, errors) — same as validate().
    """
    with open(filepath, "r") as f:
        content = f.read()
    return validate(content)


# ── Main ─────────────────────────────────────────────────────────
# You can use this to test your validator from the command line:
#   python src/json_validator.py tests/test_data/easy_correct.json

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python json_validator.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    is_valid, errors = validate_file(filepath)

    if is_valid:
        print(f"{filepath}: Valid JSON structure")
    else:
        for error in errors:
            print(error)