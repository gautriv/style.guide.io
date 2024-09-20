import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_grammar_word_choice(content, doc, suggestions):
    # Rule: Correct use of 'assure', 'ensure', 'insure'
    misuse_patterns = {
        r'\bassure\b': "Use 'assure' to mean 'to put someone's mind at ease'.",
        r'\bensure\b': "Use 'ensure' to mean 'to make certain'.",
        r'\binsure\b': "Use 'insure' only when referring to insurance."
    }
    for pattern, guidance in misuse_patterns.items():
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: {guidance}")

    # Rule: Use 'ask' instead of 'request'
    request_pattern = r'\brequest\b'
    matches = re.finditer(request_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        # Ensure 'request' is used as a verb
        if doc[match.start()].pos_ == 'VERB':
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'ask' instead of '{match.group()}' as a verb.")

    pass