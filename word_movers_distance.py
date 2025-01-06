import spacy

def spacy_similarity(text_1: str, text_2: str):
    '''
    This function calculates the similarity between two texts using the word movers distance.
    It uses the spacy library to load the pre-trained word vectors and calculate the similarity.
    The similarity is returned as a percentage.

    Arguments:
        text_1 (str): The first text to compare.
        text_2 (str): The second text to compare.
        
    Returns:
        int: The similarity between the two texts as a percentage.
        
    Raises:
        ValueError: If the spacy model is not available.
        
    '''
    print('word_movers_distance: checking similarity with spacy...')
    nlp = spacy.load("en_core_web_md")
    doc1 = nlp(text_1)
    doc2 = nlp(text_2)
    return int(doc1.similarity(doc2)*100)

   
