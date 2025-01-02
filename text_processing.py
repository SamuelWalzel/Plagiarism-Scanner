import nltk

def tokenize(text):
    print('text_processing: tokenizing...')
    tokens = nltk.word_tokenize(text)
    return tokens

def lemmatize(tokens: list):
    print('text_processing: lemmatizing...')
    lemmatized_words = []
    lemmatizer = nltk.WordNetLemmatizer()
    for word in tokens:
        lemmed_word = lemmatizer.lemmatize(word)
        lemmatized_words.append(lemmed_word.lower())
    [lemmatized_words.remove(word) for word in lemmatized_words if word.isalpha() is False]
    return lemmatized_words

def process(text):
    return lemmatize(tokenize(text))

def main():
    pass

if __name__ == '__main__':
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    main()
    
    