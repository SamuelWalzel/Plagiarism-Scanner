import nltk
from nltk.corpus import stopwords

language = 'english'

def tokenize(text):
    print('text_processing: tokenizing...')
    tokens = nltk.word_tokenize(text)
    print('text_processing: removing non-alphanumerics...')
    just_alpha_tokens = [token for token in tokens if token.isalpha() is True]
    print('text_processing: removing stopwords...')
    filtered_tokens = [token.lower() for token in just_alpha_tokens if token.lower() not in set(stopwords.words(language))]
    return filtered_tokens

def lemmatize(tokens: list):
    print('text_processing: lemmatizing...')
    lemmatized_words = []
    lemmatizer = nltk.WordNetLemmatizer()
    for word in tokens:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    return lemmatized_words

def process(text):
    return lemmatize(tokenize(text))

def main():
    pass

if __name__ == '__main__':
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('stopwords')
    main()
    
    
    