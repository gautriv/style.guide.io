import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_special_characters(content, doc, suggestions):
    # Rule 1: Use 'and' instead of '&' unless part of a formal name
    ampersand_pattern = r'&'
    matches = re.finditer(ampersand_pattern, content)
    for match in matches:
        # Check if '&' is part of a known formal name
        # For simplicity, we'll assume any '&' is incorrect unless in a formal name
        # You can expand this logic to check against a list of formal names if needed
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'and' instead of '&' unless it's part of a formal name.")
    
    # Rule 2: Use en dash for ranges, em dash for parenthetical phrases
    # Detect hyphens used in ranges
    range_pattern = r'(\d+)\s*-\s*(\d+)'
    matches = re.finditer(range_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use an en dash (–) without spaces for ranges: '{match.group()}'.")
    
    # Detect hyphens used as em dashes
    em_dash_pattern = r'\s+-\s+'
    matches = re.finditer(em_dash_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use an em dash (—) without spaces for parenthetical phrases.")
    
    # Rule 3: Proper use of ellipsis
    ellipsis_pattern = r'\.{3,}'
    matches = re.finditer(ellipsis_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use an ellipsis (…) character instead of '{match.group()}'.")
    
    # Rule 4: Correct use of quotation marks
    # Check for single quotes used as double quotes
    single_quote_pattern = r"'[^']*'"
    matches = re.finditer(single_quote_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use double quotation marks for direct quotations.")
    
    # Rule 5: Avoid overusing slashes
    slash_pattern = r'\b\w+/\w+\b'
    matches = re.finditer(slash_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid overusing slashes ('/'); consider rephrasing '{match.group()}'.")
    
    # Rule 6: Avoid using apostrophes for plurals
    apostrophe_plural_pattern = r"\b\w+'s\b"
    matches = re.finditer(apostrophe_plural_pattern, content)
    for match in matches:
        word = match.group()
        if not word.lower() in ["it's", "he's", "she's", "who's", "that's", "let's"]:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Do not use an apostrophe to form plurals: '{word}'.")
    
    # Rule 7: Use asterisks appropriately
    asterisk_pattern = r'\*'
    matches = re.finditer(asterisk_pattern, content)
    for match in matches:
        # Check context; if not used for footnotes or required fields, suggest verifying usage
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Ensure the asterisk '*' is used appropriately (e.g., footnotes, required fields).")
    
    # Rule 8: Avoid nesting parentheses
    nested_parentheses_pattern = r'\([^\(\)]*\([^\(\)]*\)[^\(\)]*\)'
    matches = re.finditer(nested_parentheses_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid nesting parentheses; consider rephrasing.")
    
    # Rule 9: Avoid using symbols in place of words
    symbol_substitutions = {
        '@': 'at',
        '#': 'number',
        '%': 'percent',
        '+': 'plus',
        '=': 'equals',
        '<': 'less than',
        '>': 'greater than'
    }
    for symbol, word in symbol_substitutions.items():
        pattern = rf'\b\w*{re.escape(symbol)}\w*\b'
        matches = re.finditer(pattern, content)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Avoid using '{symbol}' in place of words; spell out the word '{word}'.")
    
    # Rule 10: Currency symbols placement
    currency_pattern = r'(\b\d+(\.\d{1,2})?\s*(\$|€|£|¥))'
    matches = re.finditer(currency_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Place the currency symbol before the amount, e.g., '${match.group(1)}' should be formatted as '${match.group(1)}'.")
    
    pass
