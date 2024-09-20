import re
from app.utils import get_line_number

def check_cancel_terms(content, doc, suggestions):
    # Rule 1: Use "cancel" instead of "deselect" or "unmark"
    replace_terms = ["deselect", "unmark"]
    for token in doc:
        if token.text.lower() in replace_terms:
            line_number = get_line_number(content, token.idx)
            suggestions.append(f"Line {line_number}: Use 'cancel' instead of '{token.text}' when referring to canceling a selection.")

    # Rule 2: Use "clear" for checkboxes, not "cancel"
    clear_for_checkboxes_pattern = r'\b(cancel)\s+(checkbox(es)?)\b'
    matches = re.finditer(clear_for_checkboxes_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'clear' for checkboxes, not 'cancel'.")

    # Rule 3: Ensure "canceled" and "canceling" are spelled with one "l"
    misspelled_canceled_pattern = r'\bcancel(l?)ed\b'
    misspelled_canceling_pattern = r'\bcancel(l?)ing\b'

    canceled_matches = re.finditer(misspelled_canceled_pattern, content, flags=re.IGNORECASE)
    for match in canceled_matches:
        if match.group(1):  # If extra "l" is found
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Spell 'canceled' with one 'l'.")

    canceling_matches = re.finditer(misspelled_canceling_pattern, content, flags=re.IGNORECASE)
    for match in canceling_matches:
        if match.group(1):  # If extra "l" is found
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Spell 'canceling' with one 'l'.")

    # Rule 4: Ensure "cancellation" is spelled with two "l"s
    cancellation_pattern = r'\bcancel(l?)ation\b'
    matches = re.finditer(cancellation_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        if not match.group(1):  # Missing second "l"
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Spell 'cancellation' with two 'l's.")

    # Rule 5: Use "cancel" for ending processes before completion
    process_end_pattern = r'\b(cancel)\s+(the\s+process|request)\b'
    matches = re.finditer(process_end_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: 'Cancel' is correctly used here to describe ending a process or request before it's complete.")

    # Rule: Suggest replacing "unmark" with "cancel"
    unmark_pattern = r'\bunmark\b'
    matches = re.finditer(unmark_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'cancel' instead of 'unmark'.")

    # Rule: Ensure "cancel" isn't used for checkboxes
    cancel_for_checkbox_pattern = r'\b(cancel)\s+(checkbox(es)?)\b'
    matches = re.finditer(cancel_for_checkbox_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'clear' for checkboxes, not 'cancel'.")

    # Rule: Ensure "cancel" is used to end processes
    incorrect_end_terms = ["stop", "abort"]
    for token in doc:
        if token.text.lower() in incorrect_end_terms and token.head.text.lower() == "process":
            line_number = get_line_number(content, token.idx)
            suggestions.append(f"Line {line_number}: Use 'cancel' to describe ending the process, not '{token.text}'.")

