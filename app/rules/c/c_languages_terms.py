import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_c_languages_terms(content, doc, suggestions):
    # Rule 1: Ensure correct usage of 'C', 'C++', and 'C#'
    
    # Check for incorrect "C/C++" or "C/C++/C#" usage
    c_cpp_pattern = r'\bC/C\+\+/?C#?\b'
    matches = re.finditer(c_cpp_pattern, content)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Avoid using 'C/C++' or 'C/C++/C#'; refer to each language separately (e.g., 'C, C++, and C#').")

    # Check for "C-Sharp" (incorrect formatting for C#)
    csharp_pattern = r'\bC[-\s]?sharp\b'
    matches = re.finditer(csharp_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'C#' instead of '{match.group()}' when referring to the programming language.")

    # Check for lowercase 'c', 'c++', or 'c#'
    lowercase_c_patterns = {
        'c': r'\bc\b',
        'c++': r'\bc\+\+\b',
        'c#': r'\bc#\b',
    }
    
    for language, pattern in lowercase_c_patterns.items():
        matches = re.finditer(pattern, content)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Capitalize '{match.group()}' to '{language.upper()}'.")
    
    pass
