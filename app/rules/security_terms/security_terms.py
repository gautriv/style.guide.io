import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_security_terms(content, doc, suggestions):
    # Rule 1: Use 'sign in' instead of 'log in' or 'log on'
    login_patterns = [r'\blog\s?in\b', r'\blog\s?on\b']
    for pattern in login_patterns:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'sign in' instead of '{match.group()}'.")
    
    # Rule 2: Use 'malware' instead of 'virus' unless specifically referring to a virus
    virus_pattern = r'\bvirus(es)?\b'
    matches = re.finditer(virus_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        # Determine if 'virus' is being used generically
        context_window = 50  # Number of characters before and after the match
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end].lower()
        if 'trojan' in context or 'worm' in context or 'malware' in context:
            # If context includes other types of malware, suggest using 'malware'
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Consider using 'malware' instead of '{match.group()}' when referring to malware in general.")
        else:
            # If specifically about viruses, no suggestion needed
            pass
    
    # Rule 3: Use 'antimalware' instead of 'antivirus' unless specifically referring to viruses
    antivirus_pattern = r'\banti[-\s]?virus(es)?\b'
    matches = re.finditer(antivirus_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Number of characters before and after the match
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end].lower()
        # Check for general malware context
        malware_terms = ['malware', 'spyware', 'ransomware', 'trojan', 'worm', 'phishing', 'adware', 'rootkit']
        if any(term in context for term in malware_terms):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'antimalware' instead of '{match.group()}' when referring to protection against various types of malware.")
        else:
            # If specifically about viruses, no action needed
            pass

    # Rule 4: Use 'antispyware' appropriately
    antispyware_pattern = r'\banti[-\s]?spyware\b'
    matches = re.finditer(antispyware_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Number of characters before and after the match
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end].lower()
        # Check if context mentions other malware types
        if 'malware' in context or 'virus' in context or 'ransomware' in context or 'trojan' in context:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Consider using 'antimalware' instead of '{match.group()}' when referring to protection against various types of malware.")
        else:
            # If specifically about spyware, no action needed
            pass

    # Rule 5: Use 'phishing' appropriately
    phishing_pattern = r'\bphishing\b'
    matches = re.finditer(phishing_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        # No action needed unless 'phishing' is misspelled
        pass
    
    # Rule 6: Use 'two-factor authentication' or 'multifactor authentication' instead of 'two-step verification'
    two_step_pattern = r'\btwo[-\s]?step\s+verification\b'
    matches = re.finditer(two_step_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'two-factor authentication' or 'multifactor authentication' instead of '{match.group()}'.")
    
    # Rule 7: Use 'attacker' or 'unauthorized user' instead of 'hacker' unless necessary
    hacker_pattern = r'\bhacker(s)?\b'
    matches = re.finditer(hacker_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Consider using 'attacker' or 'unauthorized user' instead of '{match.group()}'.")
    
    # Rule 8: Use 'compromised' instead of 'hacked'
    hacked_pattern = r'\bhacked\b'
    matches = re.finditer(hacked_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'compromised' instead of '{match.group()}'.")
    
    # Rule 9: Use 'firewall' correctly
    firewall_pattern = r'\bfire\s+wall\b'
    matches = re.finditer(firewall_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        line_number = get_line_number(content, match.start())
        suggestions.append(f"Line {line_number}: Use 'firewall' as one word instead of '{match.group()}'.")
    
    # Rule 10: Use 'secure' instead of 'safe' when referring to security
    safe_pattern = r'\bsafe\b'
    matches = re.finditer(safe_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        context_window = 50  # Number of characters before and after the match
        start = max(0, match.start() - context_window)
        end = min(len(content), match.end() + context_window)
        context = content[start:end].lower()
        if 'secure' not in context and ('security' in context or 'protect' in context):
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Use 'secure' instead of 'safe' when referring to security.")
    
    # Rule 11: Avoid sensational or fear-mongering language
    sensational_terms = ['catastrophe', 'disaster', 'devastating', 'massive attack']
    for term in sensational_terms:
        pattern = rf'\b{term}\b'
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            line_number = get_line_number(content, match.start())
            suggestions.append(f"Line {line_number}: Avoid sensational language like '{match.group()}'. Use neutral terms.")
    
    # Rule 12: Use 'ransomware' appropriately
    ransomware_pattern = r'\bransomware\b'
    matches = re.finditer(ransomware_pattern, content, flags=re.IGNORECASE)
    for match in matches:
        # No action needed unless misused
        pass