import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    keywords = [w for w in tokens if w.isalpha() and w.lower() not in stop_words and w.lower() not in string.punctuation]
    return list(set([w.lower() for w in keywords])) 