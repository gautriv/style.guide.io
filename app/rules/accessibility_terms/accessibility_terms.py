import re
from app.utils import get_line_number
from app.utils import get_sentence_from_index

def check_accessibility_terms(content, doc, suggestions):

    # Rule 1: Use 'accessible' instead of 'disabled', 'handicapped', 'able-bodied', 'normal' (when referring to people with disabilities)
    terms_to_avoid = {
        r'\bdisabled\b': "Specify the disability if relevant or use 'accessible' for things.",
        r'\bhandicapped\b': "Use 'accessible' or specify the disability if relevant.",
        r'\bable-bodied\b': "Avoid comparing to 'able-bodied'; focus on abilities.",
        r'\bnormal\b': "Avoid using 'normal' to compare people; focus on abilities."
    }
    for pattern, suggestion in terms_to_avoid.items():
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Avoid using '{match.group()}'. {suggestion}")

    # Rule 2: Don't use 'handicap' except in proper names
    matches = re.finditer(r'\bhandicap\b', content, flags=re.IGNORECASE)
    for match in matches:
        suggestions.append(f"Avoid using '{match.group()}'; use 'accessible' or specify the disability.")

    # Rule 3: Don't use 'see', 'watch', or 'look at' to mean 'interact with'
    verbs_to_avoid = ['see', 'watch', 'look at']
    for sentence in doc.sents:
        for token in sentence:
            if token.lemma_.lower() in verbs_to_avoid:
                suggestions.append(f"Consider replacing '{token.text}' with 'interact with' or a similar term in: '{sentence.text.strip()}'")

    # Rule 4: Avoid negative terms like 'defect', 'disease', 'abnormal' when talking about disabilities
    negative_terms = [r'\bdefect\b', r'\bdisease\b', r'\babnormal\b']
    for pattern in negative_terms:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Avoid using negative terms like '{match.group()}' when discussing disabilities.")

    # Rule 5: Don't use terms that suggest pity, such as 'victim' or 'suffer from'
    pity_terms = [r'\bvictim\b', r'\bsuffer from\b']
    for pattern in pity_terms:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Avoid terms that suggest pity like '{match.group()}'; use neutral language.")

    # Rule 6: Use 'wheelchair user' instead of 'confined to a wheelchair' or 'wheelchair-bound'
    wheelchair_phrases = [r'\bconfined to a wheelchair\b', r'\bwheelchair[- ]bound\b']
    for pattern in wheelchair_phrases:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Use 'wheelchair user' instead of '{match.group()}'.")

    # Rule 7: Use person-first language
    person_first_patterns = [
        r'\bthe disabled person\b',
        r'\bthe blind\b',
        r'\bthe deaf\b',
        r'\bthe autistic\b',
    ]
    for pattern in person_first_patterns:
        matches = re.finditer(pattern, content, flags=re.IGNORECASE)
        for match in matches:
            suggestions.append(f"Use person-first language instead of '{match.group()}'; for example, 'person who is blind'.")
    
    pass