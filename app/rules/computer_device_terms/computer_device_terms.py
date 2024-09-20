import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_computer_device_terms(content, doc, suggestions):
    # Rule 1: Use 'disk' for magnetic media and 'disc' for optical media
    disk_disc_matches = re.finditer(r'\bdisc\b', content, flags=re.IGNORECASE)
    for match in disk_disc_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Ensure 'disc' is appropriate (use 'disk' for magnetic media and 'disc' for optical media).")

    # Rule 2: Use 'touchscreen' as one word
    touch_screen_matches = re.finditer(r'\btouch screen\b', content, flags=re.IGNORECASE)
    for match in touch_screen_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'touchscreen' as one word.")

    # Rule 3: Capitalize 'Internet' when used as a noun
    internet_matches = re.finditer(r'\binternet\b', content)
    for match in internet_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Capitalize 'Internet' when used as a noun.")

    # Rule 4: Use 'email' without a hyphen
    email_matches = re.finditer(r'\be-mail\b', content, flags=re.IGNORECASE)
    for match in email_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'email' without a hyphen.")

    # Rule 5: Use 'USB flash drive' instead of 'USB drive' or 'flash drive' alone
    usb_drive_matches = re.finditer(r'\b(USB drive|flash drive)\b', content, flags=re.IGNORECASE)
    for match in usb_drive_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Consider using 'USB flash drive' instead of '{match.group()}'.")
    
    # Rule 6: Use 'Ethernet' with a capital 'E'
    ethernet_matches = re.finditer(r'\bethernet\b', content)
    for match in ethernet_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Capitalize 'Ethernet'.")

    # Rule 7: Use 'Wi-Fi' with a hyphen and capital 'W' and 'F'
    wifi_matches = re.finditer(r'\bwifi\b', content, flags=re.IGNORECASE)
    for match in wifi_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'Wi-Fi' with capital 'W' and 'F' and a hyphen.")

    # Rule 8: Use 'hardware' and 'software' as uncountable nouns (avoid 'hardwares' or 'softwares')
    hardwares_softwares_matches = re.finditer(r'\b(hardwares|softwares)\b', content, flags=re.IGNORECASE)
    for match in hardwares_softwares_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'hardware' and 'software' as uncountable nouns (do not pluralize).")

    # Rule 9: Use 'computer' instead of 'machine' when referring to computers
    machine_matches = re.finditer(r'\bmachine\b', content, flags=re.IGNORECASE)
    for match in machine_matches:
        sentence = get_sentence_from_index(match.start(), doc)
        if 'computer' not in sentence.lower():
            suggestions.append(f"Line {get_line_number(content, match.start())}: Consider using 'computer' instead of 'machine' when referring to computers.")

    # Rule 10: Use 'disk space' instead of 'storage space' when referring to disk capacity
    storage_space_matches = re.finditer(r'\bstorage space\b', content, flags=re.IGNORECASE)
    for match in storage_space_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'disk space' instead of 'storage space' when referring to disk capacity.")

    # Rule 11: Use 'laptop' instead of 'notebook' when referring to portable computers
    notebook_matches = re.finditer(r'\bnotebook\b', content, flags=re.IGNORECASE)
    for match in notebook_matches:
        suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'laptop' instead of 'notebook' when referring to portable computers.")

    # Rule 12: Use 'memory' for RAM and 'storage' for disk space
    memory_storage_matches = re.finditer(r'\b(memory|storage)\b', content, flags=re.IGNORECASE)
    for match in memory_storage_matches:
        word = match.group().lower()
        sentence = get_sentence_from_index(match.start(), doc)
        if word == 'memory' and 'disk' in sentence.lower():
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'storage' instead of 'memory' when referring to disk space.")
        elif word == 'storage' and 'RAM' in sentence.upper():
            suggestions.append(f"Line {get_line_number(content, match.start())}: Use 'memory' instead of 'storage' when referring to RAM.")
    pass
