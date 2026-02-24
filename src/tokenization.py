import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

text = "Natural Language Processing is fun"
tokens = word_tokenize(text)

print(tokens)