import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_style_formatting(content, doc, suggestions):
    # Rule: Avoid using 'above' to refer to preceding content
    above_pattern = r'\babove\b'
    matches = re.finditer(above_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using 'above' to refer to previous content; use specific references.")


    # Rule: Use 'afterward' instead of 'afterwards'
    afterwards_pattern = r'\bafterwards\b'
    matches = re.finditer(afterwards_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'afterward' instead of '{match.group()}'.")


    # Rule: Avoid 'and/or'; be specific
    and_or_pattern = r'\band/or\b'
    matches = re.finditer(and_or_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using 'and/or'; consider rephrasing for clarity.")


    # Rule: Use 'and' instead of 'as well as'
    as_well_as_pattern = r'\bas\s+well\s+as\b'
    matches = re.finditer(as_well_as_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'and' instead of '{match.group()}'.")

    pass