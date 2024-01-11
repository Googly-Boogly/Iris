# import spacy
#
# nlp = spacy.load("en_core_web_sm")
#
# def process_command(command):
#     doc = nlp(command)
#     verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
#     nouns = [token.text for token in doc if token.pos_ == "NOUN"]
#     return verbs, nouns
