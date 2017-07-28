from SearchEngine import MySearchEngine
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from collect_rss import collect

__all__ = [
        "new_with",
        "most_associated_with_entity",
        "most_associated_with_phrase",
        "update_via_rss_feed"
        ]


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

    # if texts is a list, make it into a space seperated string of words
    if type(texts) != str and hasattr(texts, '__iter__'):
        texts = " ".join(texts)

    assert(type(texts) == str)

    # get id of top document
    doc_ids = search_engine.query(texts, k=1, mode="and")

    if len(doc_ids) == 0:
        return "Input phrase not found."

    best_doc_id = doc_ids[0][0]

    # get raw text
    raw_text = search_engine.get(best_doc_id)

    # tokenize raw text
    raw_tokens = word_tokenize(raw_text)

    # find index of first period in token list
    if "." not in raw_tokens:
        return " ".join(raw_tokens)

    first_period_index = raw_tokens.index(".")

    # slice token list to get first sentence, add period to end without space
    return " ".join(raw_tokens[:first_period_index]) + "."


def most_associated_with_entity(search_engine, entity, num_entities=10):
    """
    Gets the entities that are most associated with another entity.

    params:
        search_engine [MySearchEngine]:
            The search engine

        entity[string]:
            The entity that you want to find the entities associated with it.
            It can be a single words or multiple words separated by spaces.

        num_entities[int]:
            An int that describes the amount of entities returned.


    returns:
        associated_entities[List]:
            The top num_entities entities associated with the asked for entity.

    """

    associated_entities = search_engine.get_associated_entities(entity)

    return list(list(zip(*associated_entities.most_common(num_entities)))[0])


def most_associated_with_phrase(search_engine, text, num_entities=10, num_docs=10):
    """
    Gets the entities that are most associated with a phrase.

    params:
        search_engine [MySearchEngine]:
            The search engine

        text[string]:
            The phrase that you want to find the entities associated with.
            It can be a single word or multiple words separated by spaces.

        num_entities[int]:
            An int that describes the amount of entities returned.

        num_docs[int]:
            An int that describes the maximum number of documents to be searched
            through.

    returns:
        associated_entities[List]:
            The top num_entities entities associated with the asked for phrase.
    """

    # get ids of most relevant documents through query
    doc_ids = list(zip(*search_engine.query(text, k=num_docs, mode="and")))[0]

    # sum over entites vectors of all relevant documents
    accumulative_counter = Counter()
    for doc_id in doc_ids:
        accumulative_counter = accumulative_counter + search_engine.get_entity_vector(doc_id)

    # return most frequent entities in accumulative vector
    return list(list(zip(*accumulative_counter.most_common(num_entities)))[0])

def update_via_rss_feed(search_engine, rss_url):
    """
    Updates search engine with articles from the given rss feed url.

    params:
        search_engine [MySearchEngine]:
            The search engine

        rss_url [String]:
            The url of the rss feed from which to import articles.

    returns:
        updates database with new articles found from rss feed.
    """

    feed_dict = collect(rss_url, mode='return')

    for article_id in feed_dict:
        search_engine.add(article_id, feed_dict[article_id])
