import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_grammar_word_choice_b_terms(content, doc, suggestions):
    # Rule: Use 'biography' instead of 'bio' in formal contexts
    bio_pattern = r'\bbio\b'
    matches = re.finditer(bio_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'biography' instead of '{match.group()}' in formal contexts.")

    # Rule: Avoid using 'beep'; use 'sound' or 'alert' instead
    beep_pattern = r'\bbeep\b'
    matches = re.finditer(beep_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using '{match.group()}'; use 'sound' or 'alert' instead.")

