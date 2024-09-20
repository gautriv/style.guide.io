import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_cable_terms(content, doc, suggestions):
    # Rule 1: Use "cable" for physical connections; avoid using "cord" or "wire"
    cord_wire_pattern = r'\b(cord|wire)\b'
    matches = re.finditer(cord_wire_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'cable' instead of '{match.group()}' when referring to physical connections.")
    
    # Rule 2: Be specific with cable types (e.g., USB cable, Ethernet cable)
    generic_cable_pattern = r'\b(cable)\b'
    specific_cables = ['USB', 'Ethernet', 'HDMI', 'DisplayPort', 'Thunderbolt', 'VGA', 'DVI', 'power']
    
    matches = re.finditer(generic_cable_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Check nearby words for specific cable types
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        
        # If a specific cable type isn't mentioned, suggest being specific
        if not any(cable_type in context for cable_type in specific_cables):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Be specific about the cable type (e.g., 'USB cable', 'Ethernet cable').")
    
    pass
