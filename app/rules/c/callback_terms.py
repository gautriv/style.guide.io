import re
from app.utils import get_line_number

def check_callback_terms(content, doc, suggestions):
    # Rule 1: Use "call back" (two words) as a verb
    call_back_as_verb_pattern = r'\b(call\s+back)\b'
    matches = re.finditer(call_back_as_verb_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'call back' as two words when used as a verb (e.g., 'I will call you back').")
    
    # Rule 2: Use "callback" (one word) as a noun or adjective
    callback_as_noun_pattern = r'\b(callback)\b'
    matches = re.finditer(callback_as_noun_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        # Verify context, as "callback" should not be used as a verb
        line_number = get_line_number(content, match.start())
        context_window = 30
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        if 'called' in context.lower() or 'call' in context.lower():
            suggestions.append(f"Line {line_number}: Ensure 'callback' is used as a noun or adjective (e.g., 'The callback was scheduled').")
    
    # Rule 3: In developer content, avoid using "callback" to mean "callback function"
    callback_function_pattern = r'\bcallback\b'
    matches = re.finditer(callback_function_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        context_window = 30
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        if 'function' not in context.lower():
            suggestions.append(f"Line {line_number}: In developer content, avoid using 'callback' to mean 'callback function'. Use 'callback function' instead.")
    
    # Rule 4: Avoid redundant mentions of "callback function" in developer content
    callback_function_redundant_pattern = r'\bcallback function\b'
    matches = re.finditer(callback_function_redundant_pattern, content, flags=re.IGNORECASE)
    occurrences = [match.start() for match in matches]
    if len(occurrences) > 1 and any(abs(occurrences[i] - occurrences[i-1]) < 100 for i in range(1, len(occurrences))):
        line_number = get_line_number(content, occurrences[1])
        suggestions.append(f"Line {line_number}: Avoid redundant mentions of 'callback function' in close proximity.")
    pass