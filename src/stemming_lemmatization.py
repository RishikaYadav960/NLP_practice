import nltk
nltk.download('wordnet')

from nltk.stem import PorterStemmer, WordNetLemmatizer

words = ["running", "flies", "easily"]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print("Stemming:")
for w in words:
    print(stemmer.stem(w))

print("\nLemmatization:")
for w in words:
    print(lemmatizer.lemmatize(w))