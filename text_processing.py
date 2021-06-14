from nltk.stem import PorterStemmer
import string


def stemming(text, _id):
    text = "".join(l for l in text if l not in string.punctuation)
    text = ''.join([word for word in text if not word.isdigit()])   # remove numbers
    tokens = text.lower().split()                                   # lower case and splitting by spaces
    tokens = [token for token in tokens if token not in stopwords]  # remove_stopwords
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    return token_tuples(tokens, _id)


def word_stemming(word):
    return stemming(word, 0)[0][0]


def token_tuples(tokens, _id):
    return [(token.encode("utf-8"), (_id, 1, 0)) for token in tokens]


stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
             "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "cannot",
             "could", "did", "do", "does", "doing", "don't", "down", "during", "each", "few", "for", "from",
             "further", "had", "has", "have", "haven't", "having", "he", "he's", "her", "here", "hers", "herself",
             "him", "himself", "his", "hot", "how", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is",
             "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "no", "nor", "not", "of",
             "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own",
             "reuter", "same", "she", "should", "so", "some", "such", "than", "that", "that's", "the", "their",
             "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'll", "they're",
             "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't",
             "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "where", "which",
             "while", "who", "whom", "why", "with", "won't", "would", "wouldn't", "you", "you're", "your", "yours",
             "yourself"]