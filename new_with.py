from SearchEngine import MySearchEngine
import nltk
from nltk.tokenize import word_tokenize

__all__ = ["new_with"]

def new_with(search_engine, texts):

    """
    Gets the first sentence of the highest ranking document.

    param:
        search_engine [MySearchEngine]:
            The search engine

        texts[Iterable or string]:
            The thing you want to search up.

    returns:
        sentence[str]:
            The first sentence of the highest ranking document.
    """

    #if texts is a list, make it into a space seperated string of words
    if type(texts) != str and hasattr(texts, '__iter__'):
        texts = " ".join(texts)

    assert(type(texts) == str)

    #get id of top document
    doc_id = search_engine.query(texts, k=10, mode="and")[0][0]

    #get raw text
    raw_text = search_engine.get(doc_id)

    #tokenize raw text
    raw_tokens = word_tokenize(raw_text)

    #find index of first period in token list
    first_period_index = raw_tokens.index(".")

    #slice token list to get first sentence, add period to end without space
    return " ".join(raw_tokens[:first_period_index]) + "."
