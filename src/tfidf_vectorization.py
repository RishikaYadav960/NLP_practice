from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "I love NLP",
    "NLP is fun",
    "I love machine learning"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

print(vectorizer.get_feature_names_out())
print(X.toarray())
