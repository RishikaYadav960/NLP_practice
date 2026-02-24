import re

text = "NLP is Amazing!!! It helps machines understand human language."

text = text.lower()
text = re.sub(r'[^a-z\s]', '', text)

print("Cleaned Text:", text)