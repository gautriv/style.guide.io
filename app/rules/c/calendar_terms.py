import re
from app.utils import get_line_number

def check_calendar_terms(content, doc, suggestions):
    # Rule 1: Don't use 'calendar' as a verb, suggest 'schedule', 'list', or an alternative
    calendar_as_verb_pattern = r'\b(calendar(ed|ing)?)\b'
    matches = re.finditer(calendar_as_verb_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using 'calendar' as a verb. Consider using 'schedule' or 'list' instead of '{match.group()}'.")
    
    # Rule 2: Capitalize 'calendar' in product names (e.g., 'Google Calendar')
    product_name_pattern = r'\b(?:Google|Outlook)\s+calendar\b'
    matches = re.finditer(product_name_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        if 'Calendar' not in match.group():
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Ensure 'Calendar' is capitalized when used in product names (e.g., 'Google Calendar').")

    # Rule 3: Avoid redundant phrases like 'calendar schedule' or 'calendar plan'
    redundant_calendar_pattern = r'\b(calendar)\s+(schedule|plan)\b'
    matches = re.finditer(redundant_calendar_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid redundant phrases like 'calendar schedule' or 'calendar plan'. Consider using just '{match.group(1)}' or '{match.group(2)}'.")

    # Rule 4: Encourage specificity (e.g., 'event calendar', 'project calendar')
    generic_calendar_pattern = r'\bcalendar\b'
    matches = re.finditer(generic_calendar_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 30  # Check nearby words for specificity
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        if not any(specific_term in context.lower() for specific_term in ['event', 'project', 'release', 'work']):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Be specific when referring to a calendar (e.g., 'event calendar', 'project calendar').")
    
    # Rule 5: Avoid using 'calendar' in non-schedule contexts (e.g., lists or catalogs)
    non_schedule_context_pattern = r'\bcalendar\b'
    matches = re.finditer(non_schedule_context_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 30  # Check nearby words for improper usage
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        if any(term in context.lower() for term in ['items', 'list', 'catalog']):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Avoid using 'calendar' in non-schedule contexts. Consider using 'list' or 'catalog' instead.")
    pass