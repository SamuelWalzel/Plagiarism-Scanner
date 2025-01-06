import nltk
from nltk.corpus import stopwords

class Text:
    
    '''A class for processing text data.
    
    Attributes:
    
        text (str): The text to be processed.
        
        tokens (list): A list of words filtered to include only alphanumeric tokens
        
        token_count (int): The number of tokens in the text.
        
        processed (list): A list of lemmatized words.
        
        language (str): The language of the text.
        
    Methods:
    
        tokenize: Tokenizes and filters a text string into a list of meaningful words.
        
        lemmatize: Lemmatizes a list of words to their base forms.
        
        '''
    language = 'english'
    
    def __init__(self, text: str):
        
        '''
        The constructor for the Text class.
        
        Arguments:
        
            text (str): The text to be processed.
            
        '''
        
        self.text = text
        self.tokens = self.tokenize()
        self.token_count = len(self.tokens)
        self.processed = self.lemmatize()

    def tokenize(self) -> list:
        """
        Tokenizes and filters a text string into a list of meaningful words.
        
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
        tokens = nltk.word_tokenize(self.text)
        print('text_processing: removing non-alphanumerics...')
        just_alpha_tokens = [token for token in tokens if token.isalpha()]
        print('text_processing: removing stopwords...')
        filtered_tokens = [
            token.lower() for token in just_alpha_tokens 
            if token.lower() not in set(stopwords.words(Text.language))
        ]
        return filtered_tokens


    def lemmatize(self) -> list:
        """
        Lemmatizes a list of words to their base forms.

        Returns:
            list: A list of lemmatized words.

        Steps:
            1. Iterates through the list of tokens.
            2. Applies NLTK's WordNetLemmatizer to each word to find its base form.
        """
        print('text_processing: lemmatizing...')
        lemmatized_words = []
        lemmatizer = nltk.WordNetLemmatizer()
        for word in self.tokens:
            lemmatized_words.append(lemmatizer.lemmatize(word))
        return lemmatized_words
    
def from_path(path: str) -> Text:
    """
    Reads text from a file and creates a Text object.

    Arguments:
        path (str): The path to the file to be read.

    Returns:
        Text: A Text object created from the text in the file.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        print('text_processing: reading from file...')
        with open(path) as file:
            return Text(file.read())
    except FileNotFoundError:
        print('text_processing: file not found')
        raise FileNotFoundError

def main():
    pass

if __name__ == '__main__':
    nltk.download('punkt_tab')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('stopwords')
    main()
    
    
    