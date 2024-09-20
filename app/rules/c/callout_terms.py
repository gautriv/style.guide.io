import re
from app.utils import get_line_number

def check_callout_terms(content, doc, suggestions):
    # Rule 1: Use "call out" (two words) as a verb
    for token in doc:
        if token.text.lower() == "call" and token.head.text.lower() == "out" and token.dep_ == "ROOT" and token.head.dep_ == "prt":
            sentence = token.sent.text
            line_number = get_line_number(content, token.idx)
            suggestions.append(f"Line {line_number}: Use 'call out' as two words when used as a verb (e.g., 'She will call out the names').")

    # Rule 2: Use "callout" (one word) as a noun or adjective
    callout_pattern = r'\b(callout)\b'
    matches = re.finditer(callout_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Ensure 'callout' is used as a noun or adjective (e.g., 'The callout was clear').")

    # Rule 3: Avoid "callout" when used as a verb
    callout_as_verb_pattern = r'\b(callout)\s+\w+ing\b'
    matches = re.finditer(callout_as_verb_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using 'callout' as a verb. Use 'call out' instead.")

    # Rule: Detect passive voice use of 'call out'
    for token in doc:
        if token.text.lower() == "called" and token.head.dep_ == "auxpass":
            sentence = token.sent.text
            line_number = get_line_number(content, token.idx)
            suggestions.append(f"Line {line_number}: Consider rephrasing 'call out' in active voice.")

    pass
