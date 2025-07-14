import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

import os

nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('stopwords', download_dir=nltk_data_dir)

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    keywords = [w for w in tokens if w.isalpha() and w.lower() not in stop_words and w.lower() not in string.punctuation]
    return list(set([w.lower() for w in keywords])) 