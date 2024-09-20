import re
from collections import defaultdict
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_units_of_measure_terms(content, doc, suggestions):
    # Rule 1: Use numerals for numbers with units
    number_with_unit_pattern = r'\b(one|two|three|four|five|six|seven|eight|nine|ten)\s+(cm|mm|kg|g|lbs|pounds|kilograms|meters|metres|miles|inches|inch|feet|ft|kilometers|kilometres|hours|minutes|seconds)\b'
    matches = re.finditer(number_with_unit_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        number_word = match.group(1)
        unit = match.group(2)
        numeral = str(convert_number_word_to_numeral(number_word.lower()))
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use numerals for numbers with units: '{match.group()}' should be '{numeral} {unit}'.")
    
    # Rule 2: Use standard abbreviations without periods
    units_with_periods_pattern = r'\b(\d+)\s*(cm\.|mm\.|kg\.|g\.|lb\.|lbs\.|m\.|km\.|sec\.|min\.)\b'
    matches = re.finditer(units_with_periods_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        number = match.group(1)
        unit = match.group(2).replace('.', '')
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Remove the period from unit abbreviations: '{match.group()}' should be '{number} {unit}'.")
    
    # Rule 3: Use singular form for 1 unit and plural for more than 1
    singular_plural_pattern = r'\b1\s+(\w+?)(s)?\b'
    matches = re.finditer(singular_plural_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        unit = match.group(1)
        plural_s = match.group(2)
        if plural_s:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use singular form for 1 unit: '{match.group()}' should be '1 {unit}'.")
    
    # Rule 4: No space between number and % sign
    percent_pattern = r'\b(\d+)\s+%\b'
    matches = re.finditer(percent_pattern, content)
    for match in matches:
        number = match.group(1)
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Remove space between number and '%': '{match.group()}' should be '{number}%'.")
    
    # Rule 5: Use 'per' instead of slash (/) in units
    per_units_pattern = r'\b(\w+/h|km/h|m/s|mb/s|gb/s|kb/s)\b'
    matches = re.finditer(per_units_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        unit = match.group()
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'per' instead of '/': '{unit}' should be written out (e.g., 'kilometers per hour').")
    
    # Rule 6: Spell out units of time in text
    time_units_pattern = r'\b(\d+)\s*(hrs|hr|mins|min|sec|secs)\b'
    matches = re.finditer(time_units_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        number = match.group(1)
        unit = match.group(2)
        unit_full = convert_time_unit_to_full_form(unit.lower())
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Spell out units of time in text: '{match.group()}' should be '{number} {unit_full}'.")
    
    # Rule 7: Use degree symbol with temperature units, no space between number and symbol
    temperature_pattern = r'\b(\d+)\s?(°\s?[CF])\b'
    matches = re.finditer(temperature_pattern, content)
    for match in matches:
        number = match.group(1)
        degree_unit = match.group(2).replace(' ', '')
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Remove space between number and degree symbol: '{match.group()}' should be '{number}{degree_unit}'.")
    
    # Rule 8: Be consistent with units throughout the document
    # Collect all units used in the document
    unit_patterns = r'\b\d+\.?\d*\s*(cm|mm|kg|g|lbs|pounds|kilograms|meters|metres|miles|inches|inch|feet|ft|kilometers|kilometres|km|hours|hrs|minutes|min|seconds|sec)\b'
    unit_matches = re.finditer(unit_patterns, content, flags=re.IGNORECASE)
    units_found = defaultdict(list)  # Dictionary to store units and their occurrences
    
    for match in unit_matches:
        unit = match.group(1).lower()
        position = match.start()
        line_number = get_line_number(content, position)
        units_found[unit].append(line_number)
    
    # Identify inconsistent units for the same measurement type
    measurement_types = {
        'length': ['cm', 'mm', 'meters', 'metres', 'miles', 'inches', 'inch', 'feet', 'ft', 'kilometers', 'kilometres', 'km'],
        'weight': ['kg', 'kilograms', 'g', 'lbs', 'pounds'],
        'time': ['hours', 'hrs', 'minutes', 'min', 'seconds', 'sec'],
    }
    
    for measurement, unit_list in measurement_types.items():
        units_in_document = [unit for unit in units_found.keys() if unit in unit_list]
        if len(units_in_document) > 1:
            # Inconsistency found
            lines = []
            for unit in units_in_document:
                lines.extend(units_found[unit])
            lines = sorted(set(lines))
            lines_str = ', '.join(map(str, lines))
            suggestions.append(f"Lines {lines_str}: Inconsistent units of {measurement} found: {', '.join(units_in_document)}. Consider using consistent units throughout the document.")
    
    # Rule 9: Avoid obsolete units; prefer SI units
    obsolete_units = ['inches', 'inch', 'feet', 'ft', 'pounds', 'lbs']
    for unit in obsolete_units:
        pattern = rf'\b\d+\.?\d*\s*{unit}\b'
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Consider using SI units instead of '{unit}'.")
    
    # Rule 10: Currency symbols placement
    currency_pattern = r'(\b\d+(\.\d{1,2})?\s*(\$|€|£|¥))'
    matches = re.finditer(currency_pattern, content)
    for match in matches:
        number = match.group(1)
        symbol = match.group(3)
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Place the currency symbol before the amount: '{match.group()}' should be '{symbol}{number}'.")
    
    # Helper functions
    def convert_number_word_to_numeral(word):
        number_words = {
            'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
            'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10
        }
        return number_words.get(word, word)
    
    def convert_time_unit_to_full_form(abbreviation):
        time_units = {
            'hr':'hour', 'hrs':'hours',
            'min':'minute', 'mins':'minutes',
            'sec':'second', 'secs':'seconds'
        }
        return time_units.get(abbreviation, abbreviation)
    
    pass