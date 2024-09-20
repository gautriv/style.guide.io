import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_dimensional_terms(content, doc, suggestions):
    # Rule 1: Use "2D" as an adjective before a noun, "two-dimensional" elsewhere
    two_d_pattern = r'\b(two[-\s]?dimensional|2D)\b'
    matches = re.finditer(two_d_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        term = match.group()
        start_pos = match.start()
        line_number = get_line_number(content, start_pos)

        # Look ahead to see if it's directly before a noun
        after_term = content[match.end():match.end()+20]
        noun_match = re.match(r'\s*\w+', after_term)
        if noun_match:
            noun = noun_match.group().strip()
            if noun:
                # It's before a noun; use "2D"
                if term.lower() != '2d':
                    suggestions.append(f"Line {line_number}: Use '2D' before a noun instead of '{term}'.")
            else:
                # Not before a noun; use "two-dimensional"
                if term.lower() != 'two-dimensional':
                    suggestions.append(f"Line {line_number}: Use 'two-dimensional' when not before a noun.")
        else:
            # Not before a noun; use "two-dimensional"
            if term.lower() != 'two-dimensional':
                suggestions.append(f"Line {line_number}: Use 'two-dimensional' when not before a noun.")

    # Rule 2: Use "3D" as an adjective before a noun, "three-dimensional" elsewhere
    three_d_pattern = r'\b(three[-\s]?dimensional|3D)\b'
    matches = re.finditer(three_d_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        term = match.group()
        start_pos = match.start()
        line_number = get_line_number(content, start_pos)

        # Look ahead to see if it's directly before a noun
        after_term = content[match.end():match.end()+20]
        noun_match = re.match(r'\s*\w+', after_term)
        if noun_match:
            noun = noun_match.group().strip()
            if noun:
                # It's before a noun; use "3D"
                if term.lower() != '3d':
                    suggestions.append(f"Line {line_number}: Use '3D' before a noun instead of '{term}'.")
            else:
                # Not before a noun; use "three-dimensional"
                if term.lower() != 'three-dimensional':
                    suggestions.append(f"Line {line_number}: Use 'three-dimensional' when not before a noun.")
        else:
            # Not before a noun; use "three-dimensional"
            if term.lower() != 'three-dimensional':
                suggestions.append(f"Line {line_number}: Use 'three-dimensional' when not before a noun.")

    # Rule 3: Use "8.5 x 11-inch paper" and format dimensions correctly
    dimension_pattern = r'\b(\d+\.?\d*)\s*[xX×]\s*(\d+\.?\d*)\s*(inch|inches|in\.?)?\s*(paper)?\b'
    matches = re.finditer(dimension_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        width = match.group(1)
        height = match.group(2)
        unit = match.group(3)
        noun = match.group(4)
        line_number = get_line_number(content, match.start())

        # Build the correct phrase
        correct_phrase = f"{width} x {height}-inch"
        if noun:
            correct_phrase += f" {noun.strip()}"
        suggestions.append(f"Line {line_number}: Use '{correct_phrase}' to refer to dimensions. Include units and hyphenate appropriately.")

    pass
