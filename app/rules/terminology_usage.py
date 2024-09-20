import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_terminology_usage(content, doc, suggestions):
    # Rule: Avoid 'abort' or 'abortion'; use 'cancel' or 'stop' instead
    abort_pattern = r'\babort(ion)?\b'
    matches = re.finditer(abort_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using '{match.group()}'; use 'cancel' or 'stop' instead.")


    # Rule: Use 'accessible' appropriately
    accessible_pattern = r'\baccessible\b'
    matches = re.finditer(accessible_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Number of characters before and after the match
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end].lower()

        # Check if 'accessible' is used in the context of accessibility
        accessibility_terms = [
            'disability', 'disabilities', 'assistive', 'accessibility',
            'wheelchair', 'hearing', 'vision', 'blind', 'deaf',
            'screen reader', 'voiceover', 'narrator', 'high contrast',
            'keyboard navigation', 'inclusive design', 'universal design'
        ]

        # If none of the accessibility terms are in the context, flag it
        if not any(term in context for term in accessibility_terms):
            line_number = get_line_number(content, match.start())
            suggestions.append(
                f"Line {line_number}: Ensure 'accessible' is used to refer to content usable by people with disabilities."
            )


    # Rule: Use 'administrator' instead of 'admin' in text
    admin_pattern = r'\badmin\b'
    matches = re.finditer(admin_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'administrator' instead of '{match.group()}' in content.")


    # Rule: Use 'app' vs. 'application' correctly
    # Find occurrences of 'app' and 'application'
    app_pattern = r'\bapp\b'
    application_pattern = r'\bapplication\b'

    # Process 'app' occurrences
    app_matches = re.finditer(app_pattern, content, flags=re.IGNORECASE)
    for match in app_matches:
        context_window = 50
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end].lower()

        # Heuristic to detect complex software context
        complex_terms = ['enterprise', 'complex', 'system', 'software', 'suite', 'platform', 'desktop']
        if any(term in context for term in complex_terms):
            line_number = get_line_number(content, match.start())
            suggestions.append(
                f"Line {line_number}: Consider using 'application' instead of 'app' for complex software."
            )

    # Process 'application' occurrences
    application_matches = re.finditer(application_pattern, content, flags=re.IGNORECASE)
    for match in application_matches:
        context_window = 50
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end].lower()

        # Heuristic to detect simple software context
        simple_terms = ['mobile', 'simple', 'small', 'game', 'tool', 'widget', 'device']
        if any(term in context for term in simple_terms):
            line_number = get_line_number(content, match.start())
            suggestions.append(
                f"Line {line_number}: Consider using 'app' instead of 'application' for simple or mobile software."
            )


    # Rule: Use 'auto' as a prefix; avoid standalone use
    auto_pattern = r'\bauto\b'
    matches = re.finditer(auto_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        # Check if 'auto' is used standalone
        context = content[max(0, match.start()-10):match.end()+10]
        if not re.search(r'\bauto\w+', context):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'automatic' instead of 'auto' when used as an adjective.")

    pass