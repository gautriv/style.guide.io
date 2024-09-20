import spacy
from .rules import rule_functions
from .utils import get_line_number, get_sentence_from_index

nlp = spacy.load("en_core_web_sm")

def analyze_content(content):
    doc = nlp(content)
    suggestions = []

    # Call each rule function
    for rule_function in rule_functions:
        rule_function(content, doc, suggestions)

    return suggestions