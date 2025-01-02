import nltk
from nltk.corpus import stopwords

language = 'english'

def tokenize(text: str) -> list:
    """
    Tokenizes and filters a text string into a list of meaningful words.

    Arguments:
        text (str): The text to be processed.

    Returns:
        list: A list of words filtered to include only alphanumeric tokens 
              (excluding stopwords and non-alphanumeric characters).

    Steps:
        1. Splits the text into tokens using NLTK's word_tokenize.
        2. Filters out tokens that are not alphabetic.
        3. Removes stopwords for the specified language and converts tokens to lowercase.

    Raises:
        ValueError: If `stopwords` or the specified language is unavailable in NLTK.
    """
    print('text_processing: tokenizing...')
    tokens = nltk.word_tokenize(text)
    print('text_processing: removing non-alphanumerics...')
    just_alpha_tokens = [token for token in tokens if token.isalpha()]
    print('text_processing: removing stopwords...')
    filtered_tokens = [
        token.lower() for token in just_alpha_tokens 
        if token.lower() not in set(stopwords.words(language))
    ]
    return filtered_tokens


def lemmatize(tokens: list) -> list:
    """
    Lemmatizes a list of words to their base forms.

    Arguments:
        tokens (list): A list of words to be lemmatized.

    Returns:
        list: A list of lemmatized words.

    Steps:
        1. Iterates through the list of tokens.
        2. Applies NLTK's WordNetLemmatizer to each word to find its base form.
    """
    print('text_processing: lemmatizing...')
    lemmatized_words = []
    lemmatizer = nltk.WordNetLemmatizer()
    for word in tokens:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    return lemmatized_words


def process(text: str) -> list:
    """
    Processes a text string by tokenizing and lemmatizing it.

    Arguments:
        text (str): The text to be processed.

    Returns:
        list: A list of processed words, filtered, and reduced to their base forms.

    Steps:
        1. Tokenizes the input text by removing stopwords and non-alphanumeric tokens.
        2. Lemmatizes the tokens to their base forms using the `lemmatize` function.
    """
    return lemmatize(tokenize(text))

def main():
    pass

if __name__ == '__main__':
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('stopwords')
    main()
    
    
    