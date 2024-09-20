import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_cabling_terms(content, doc, suggestions):
    # Rule 1: Use "cabling" instead of "wiring" when referring to a system of cables
    wiring_pattern = r'\bwiring\b'
    matches = re.finditer(wiring_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'cabling' instead of 'wiring' when referring to a system of cables.")
    
    # Rule 2: Be specific about the type of cabling (e.g., network cabling, fiber-optic cabling)
    generic_cabling_pattern = r'\bcabling\b'
    specific_cabling_types = ['network', 'fiber-optic', 'structured', 'coaxial', 'Ethernet', 'power']
    
    matches = re.finditer(generic_cabling_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Check nearby words for specific cabling types
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        
        # If a specific cabling type isn't mentioned, suggest being specific
        if not any(cabling_type in context for cabling_type in specific_cabling_types):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Be specific about the type of cabling (e.g., 'network cabling', 'fiber-optic cabling').")
    
    pass
