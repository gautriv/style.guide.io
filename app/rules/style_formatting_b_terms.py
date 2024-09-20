import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_style_formatting_b_terms(content, doc, suggestions):
    # Rule: Avoid using 'below' to refer to subsequent content
    below_pattern = r'\bbelow\b'
    matches = re.finditer(below_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using 'below' to refer to subsequent content; use specific references.")

    # Rule: Use 'bps' in lowercase for bits per second
    bps_pattern = r'\b[Bb]ps\b'
    matches = re.finditer(bps_pattern, content)
    for match in matches:
        if match.group() != 'bps':
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'bps' in lowercase for bits per second.")

    # Rule: Hyphenate 'bottom-left' and 'bottom-right' when used before a noun
    position_pattern = r'\b(bottom left|bottom right)\s+\w+'
    matches = re.finditer(position_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        term = match.group(1)
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Hyphenate '{term}' when used as an adjective before a noun (e.g., 'bottom-left corner').")

    pass