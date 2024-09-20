import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_technical_terms(content, doc, suggestions):
    # Rule: Capitalize 'Bluetooth'
    bluetooth_pattern = r'\bbluetooth\b'
    matches = re.finditer(bluetooth_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Capitalize 'Bluetooth' as it's a proper noun.")

    # Rule: Use 'bounding box' instead of 'bounding outline'
    bounding_outline_pattern = r'\bbounding outline\b'
    matches = re.finditer(bounding_outline_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'bounding box' instead of '{match.group()}'.")

    # Rule: Use 'Blu-ray Disc' with correct capitalization
    bluray_pattern = r'\bblu[-\s]?ray\s+disc\b'
    matches = re.finditer(bluray_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        if match.group() != 'Blu-ray Disc':
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'Blu-ray Disc' with 'Disc' capitalized.")

    pass