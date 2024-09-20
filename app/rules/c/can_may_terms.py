import re
from app.utils import get_line_number

def check_can_may_terms(content, doc, suggestions):
    # Rule 1: Check for unnecessary use of "can"
    for token in doc:
        if token.text.lower() == "can" and token.dep_ == "aux":
            sentence = token.sent.text
            line_number = get_line_number(content, token.idx)
            # Suggest rephrasing if possible
            suggestions.append(f"Line {line_number}: Consider rewriting to describe the action instead of using 'can'.")
    
    # Rule 2: Check for proper use of "may" and suggest replacing it with "might"
    may_pattern = r'\bmay\b'
    matches = re.finditer(may_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using 'may' as it can imply permission. Consider using 'might' to express possibility.")

    # Rule 3: Ensure "could" is used only for the past and not as a substitute for "can"
    could_pattern = r'\bcould\b'
    matches = re.finditer(could_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        context_window = 30
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        if "past" not in context.lower():
            suggestions.append(f"Line {line_number}: Ensure 'could' is only used to describe the past. Use 'can' for present actions.")

    # Rule: Detect overuse of "can" and suggest rewording
    can_count = len([token for token in doc if token.text.lower() == "can"])
    if can_count > 3:  # Threshold for overuse (customizable)
        suggestions.append("Consider rephrasing to avoid overusing 'can'.")


    # Rule: Detect "can" being used to express permission
    for token in doc:
        if token.text.lower() == "can" and "permission" in token.sent.text.lower():
            line_number = get_line_number(content, token.idx)
            suggestions.append(f"Line {line_number}: Avoid using 'can' to express permission. Consider using 'allowed to' or 'able to'.")


    pass