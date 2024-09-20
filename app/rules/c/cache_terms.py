import re
from app.utils import get_line_number


def check_cache_terms(content, doc, suggestions):
    # Rule 1: Ensure "disk cache" is used when referring to cache on a hard disk or SSD
    generic_cache_pattern = r'\b(cache)\b'
    disk_cache_terms = ['hard disk', 'SSD', 'disk', 'storage', 'disk drive']
    
    matches = re.finditer(generic_cache_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Check nearby words for disk-related context
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        
        # If any disk-related term is found, suggest using "disk cache"
        if any(term in context for term in disk_cache_terms):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'disk cache' instead of 'cache' when referring to a disk-based cache (e.g., on a hard disk or SSD).")
    
    # Rule 2: Ensure "cache" is used correctly for memory-based cache
    disk_cache_pattern = r'\bdisk\s+cache\b'
    memory_cache_terms = ['memory', 'RAM', 'CPU cache', 'L1 cache', 'L2 cache', 'L3 cache']
    
    matches = re.finditer(disk_cache_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Check nearby words for memory-related context
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end]
        
        # If memory-related terms are found, suggest using "cache" instead of "disk cache"
        if any(term in context for term in memory_cache_terms):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'cache' instead of 'disk cache' when referring to memory-based caching (e.g., in RAM or CPU).")
    pass