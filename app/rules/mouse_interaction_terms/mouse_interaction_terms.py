import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_mouse_interaction_terms(content, doc, suggestions):
    # Rule 1: Use 'select' instead of 'click' for UI elements
    click_matches = re.finditer(r'\bclick\b', content, flags=re.IGNORECASE)
    for match in click_matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'select' instead of 'click' when referring to UI elements.")

    # Rule 2: Use 'point to' instead of 'hover over' or 'mouse over'
    hover_terms = ['hover over', 'mouse over', 'hover']
    for term in hover_terms:
        pattern = rf'\b{term}\b'
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'point to' instead of '{match.group()}'.")

    # Rule 3: Use 'drag' and 'drop' appropriately
    # Ensure 'drag and drop' is used correctly
    drag_drop_pattern = r'\bdrag\s+and\s+drop\b'
    matches = re.finditer(drag_drop_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        # No action needed; 'drag and drop' is acceptable
        pass

    # Check for incorrect usage of 'drag' and 'drop'
    drag_matches = re.finditer(r'\bdrag\b', content, flags=re.IGNORECASE)
    for match in drag_matches:
        # Ensure 'drag' is used correctly (e.g., not 'drag the mouse')
        context = content[max(0, match.start()-10):match.end()+10].lower()
        if 'mouse' in context:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'drag' without mentioning the mouse, e.g., 'drag the item'.")

    drop_matches = re.finditer(r'\bdrop\b', content, flags=re.IGNORECASE)
    for match in drop_matches:
        # Ensure 'drop' is used correctly
        # Generally acceptable; no action needed unless misused

        # Optional: You can add checks if needed

        pass

    # Rule 4: Use 'right-click' and 'double-click' with a hyphen
    click_terms = {'right click': 'right-click', 'double click': 'double-click'}
    for incorrect, correct in click_terms.items():
        pattern = rf'\b{incorrect}\b'
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use '{correct}' with a hyphen instead of '{match.group()}'.")

    # Rule 5: Avoid unnecessary mentions of the mouse
    mouse_phrases = [r'\bwith\s+the\s+mouse\b', r'\busing\s+the\s+mouse\b']
    for pattern in mouse_phrases:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Avoid mentioning the mouse unless necessary. Remove '{match.group()}'.")

    # Rule 6: Be inclusive of different input methods
    # Avoid phrases like 'click with your mouse' or 'mouse over'
    inclusive_terms = [r'\bclick\s+with\s+your\s+mouse\b', r'\bmouse\s+over\b']
    for pattern in inclusive_terms:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use inclusive language that accommodates different input methods.")

    # Rule 7: Avoid anthropomorphizing the mouse
    # Phrases like 'the mouse wants you to...'
    anthropomorphic_patterns = [r'\bmouse\s+(\w+\s+){0,3}(want|needs|asks)\b']
    for pattern in anthropomorphic_patterns:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Avoid anthropomorphizing the mouse. Rephrase '{match.group()}'.")

    # Rule 8: Use 'scroll' appropriately
    scroll_matches = re.finditer(r'\bscroll\b', content, flags=re.IGNORECASE)
    for match in scroll_matches:
        # Ensure 'scroll' is used to refer to moving content, not the mouse wheel
        context = content[max(0, match.start()-20):match.end()+20].lower()
        if 'mouse' in context and 'wheel' in context:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'scroll' to refer to moving content, not the mouse wheel.")

    # Rule 9: Avoid 'click on'; use 'select'
    click_on_pattern = r'\bclick\s+on\b'
    matches = re.finditer(click_on_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'select' instead of 'click on'.")

    # Rule 10: Use 'press and hold' instead of 'click and hold'
    click_hold_pattern = r'\bclick\s+and\s+hold\b'
    matches = re.finditer(click_hold_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'press and hold' instead of 'click and hold'.")

    pass
