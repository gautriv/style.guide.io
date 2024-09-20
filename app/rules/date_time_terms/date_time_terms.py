import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_date_time_terms(content, doc, suggestions):
    # Rule 1: Use numerals for dates (e.g., 'January 1, 2020')
    date_ordinal_patterns = [
        r'\bJanuary \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bFebruary \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bMarch \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bApril \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bMay \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bJune \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bJuly \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bAugust \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bSeptember \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bOctober \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bNovember \d{1,2}(st|nd|rd|th), \d{4}\b',
        r'\bDecember \d{1,2}(st|nd|rd|th), \d{4}\b',
    ]
    for pattern in date_ordinal_patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            suggestions.append(f"Line {get_line_number(content, match.start())}: Remove ordinal indicators (st, nd, rd, th) in dates: '{match.group()}'. Use 'January 1, 2020' format.")

    # Rule 2: Do not use ordinals with dates (e.g., '1st', '2nd', '3rd')
    ordinal_date_matches = re.finditer(r'\b\d{1,2}(st|nd|rd|th)\b', content)
    for match in ordinal_date_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Avoid using ordinals with dates: '{match.group()}'. Use numerals without ordinals.")

    # Rule 3: Use 'a.m.' and 'p.m.' in lowercase with periods
    time_matches = re.finditer(r'\b\d{1,2}(:\d{2})?\s*(AM|PM|A\.M\.|P\.M\.|am|pm|a\.m\.|p\.m\.)\b', content)
    for match in time_matches:
        time_str = match.group()
        if not re.search(r'\b(a\.m\.|p\.m\.)\b', time_str, flags=re.IGNORECASE):
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'a.m.' or 'p.m.' in lowercase with periods: '{time_str}'.")
        elif re.search(r'\b(A\.M\.|P\.M\.)\b', time_str):
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'a.m.' or 'p.m.' in lowercase: '{time_str}'.")

    # Rule 4: Avoid redundancies like '12 noon' or '12 midnight'; use 'noon' or 'midnight'
    redundancies = {
        r'\b12\s?(noon)\b': "Use 'noon' without '12'.",
        r'\b12\s?(midnight)\b': "Use 'midnight' without '12'.",
        r'\b(noon\s?12)\b': "Use 'noon' without '12'.",
        r'\b(midnight\s?12)\b': "Use 'midnight' without '12'."
    }
    for pattern, suggestion_text in redundancies.items():
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Line {get_line_number(content, match.start())}: {suggestion_text}")

    # Rule 5: Use 24-hour clock format without 'a.m.' or 'p.m.' if specified
    time_24hr_matches = re.finditer(r'\b([01]?\d|2[0-3]):[0-5]\d\b', content)
    for match in time_24hr_matches:
        time_str = match.group()
        # Check if 'a.m.' or 'p.m.' is mistakenly used with 24-hour format
        following_text = content[match.end():match.end()+5]
        if re.search(r'\s*(a\.m\.|p\.m\.)', following_text, flags=re.IGNORECASE):
            suggestions.append(f"Line {get_line_number(content, match.start())}: Do not use 'a.m.' or 'p.m.' with 24-hour time format: '{time_str}{following_text.strip()}'.")

    # Rule 6: Write dates in 'Month Day, Year' format (e.g., 'January 1, 2020')
    incorrect_date_formats = [
        r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',  # e.g., '1/1/2020'
        r'\b\d{1,2}-\d{1,2}-\d{2,4}\b',  # e.g., '1-1-2020'
        r'\b\d{4}-\d{1,2}-\d{1,2}\b',    # e.g., '2020-1-1'
        r'\b\d{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December),?\s\d{4}\b'  # e.g., '1 January 2020'
    ]
    for pattern in incorrect_date_formats:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'Month Day, Year' format for dates: '{match.group()}'. For example, 'January 1, 2020'.")

    # Rule 7: Avoid using 'today', 'tomorrow', 'yesterday'; use specific dates
    relative_dates = ['today', 'tomorrow', 'yesterday']
    for word in relative_dates:
        matches = re.finditer(rf'\b{word}\b', content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Line {get_line_number(content, match.start())}: Avoid using relative dates like '{match.group()}'; use specific dates for clarity.")

    # Rule 8: Use 'through' instead of en dash or hyphen in date ranges
    date_range_patterns = [
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}\s?[-–]\s?\d{1,2},\s\d{4}\b',
        r'\b\d{1,2}\s?[-–]\s?\d{1,2}\s(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b'
    ]
    for pattern in date_range_patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'through' instead of a dash in date ranges: '{match.group()}'. For example, 'January 1 through 5, 2020'.")

    # Rule 9: Do not use '00' minutes in times; use '1 p.m.' instead of '1:00 p.m.'
    zero_minutes_matches = re.finditer(r'\b(\d{1,2}):00\s?(a\.m\.|p\.m\.)\b', content, flags=re.IGNORECASE)
    for match in zero_minutes_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Omit ':00' in times: '{match.group()}'. Use '{match.group(1)} {match.group(2)}' instead.")

    # Rule 10: Use 'midnight' instead of '12 a.m.' and 'noon' instead of '12 p.m.'
    midnight_noon_matches = re.finditer(r'\b12\s?(a\.m\.|p\.m\.)\b', content, flags=re.IGNORECASE)
    for match in midnight_noon_matches:
        if 'a.m.' in match.group().lower():
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'midnight' instead of '12 a.m.'.")
        else:
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'noon' instead of '12 p.m.'.")
    pass
