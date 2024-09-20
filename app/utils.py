def get_line_number(content, index):
    return content.count('\n', 0, index) + 1

def get_sentence_from_index(index, doc):
    for sent in doc.sents:
        if sent.start_char <= index <= sent.end_char:
            return sent.text
    return ''

