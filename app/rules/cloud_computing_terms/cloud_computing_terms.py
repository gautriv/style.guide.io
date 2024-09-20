import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_cloud_computing_terms(content, doc, suggestions):
    # Rule 1: Use 'on-premises' instead of 'on-premise' when referring to location
    matches = re.finditer(r'\bon-premise\b', content, flags=re.IGNORECASE)
    for match in matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'on-premises' instead of '{match.group()}'.")
    
    # Rule 2: Use 'cloud computing' without hyphens
    matches = re.finditer(r'\bcloud-computing\b', content, flags=re.IGNORECASE)
    for match in matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'cloud computing' without a hyphen.")
    
    # Rule 3: Use 'cloud' as a noun or adjective, avoid 'cloud-based'
    matches = re.finditer(r'\bcloud-based\b', content, flags=re.IGNORECASE)
    for match in matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Consider using 'cloud' as a noun or adjective instead of 'cloud-based'.")
    
    # Rule 4: Use 'virtual machine (VM)' on first mention
    vm_mentions = [match.start() for match in re.finditer(r'\bVM\b', content)]
    if vm_mentions:
        first_vm_index = vm_mentions[0]
        prior_content = content[:first_vm_index]
        if not re.search(r'virtual machine', prior_content, flags=re.IGNORECASE):
            suggestions.append("Spell out 'virtual machine (VM)' on first mention.")
    
    # Rule 5: Use 'service' instead of 'services' when referring to a single service
    services_matches = re.finditer(r'\bservices\b', content, flags=re.IGNORECASE)
    for match in services_matches:
        # Check if 'services' is being used in singular context
        sentence = get_sentence_from_index(match.start(), doc)
        if re.search(r'\b(an|a|one)\s+services\b', sentence, flags=re.IGNORECASE):
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'service' instead of 'services' when referring to a single service.")
    
    # Rule 6: Use 'cloud computing' instead of 'the cloud' when appropriate
    matches = re.finditer(r'\bthe cloud\b', content, flags=re.IGNORECASE)
    for match in matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Consider using 'cloud computing' instead of '{match.group()}' for clarity.")
    
    # Rule 7: Avoid 'in the cloud'; use 'with cloud computing' or 'on cloud platforms'
    matches = re.finditer(r'\bin the cloud\b', content, flags=re.IGNORECASE)
    for match in matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Consider rephrasing '{match.group()}' to 'with cloud computing' or 'on cloud platforms'.")
    
    # Rule 8: Use 'cloud services' when referring to services provided via cloud computing
    matches = re.finditer(r'\bcloud service\b', content, flags=re.IGNORECASE)
    for match in matches:
        # Check if plural 'cloud services' is more appropriate
        suggestions.append(f"Line {get_line_number(content, match.start())}: Ensure that 'cloud service' is correctly singular or consider 'cloud services' if plural is needed.")
    
    # Rule 9: Avoid using 'hybrid cloud' as a noun; use it as an adjective
    matches = re.finditer(r'\bhybrid cloud\b', content, flags=re.IGNORECASE)
    for match in matches:
        sentence = get_sentence_from_index(match.start(), doc)
        if not re.search(r'\bhybrid cloud\b\s+\w+', sentence):
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'hybrid cloud' as an adjective, not as a standalone noun.")
    
    # Rule 10: Use 'multi-cloud' with a hyphen when used as an adjective
    matches = re.finditer(r'\bmulticloud\b', content, flags=re.IGNORECASE)
    for match in matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'multi-cloud' with a hyphen when used as an adjective.")
        
    pass
