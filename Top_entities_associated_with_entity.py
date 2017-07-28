from collections import defaultdict, Counter
from SearchEngine import MySearchEngine
import nltk
from nltk.tokenize import word_tokenize

# Try what we did on Wednesday with the sliding window thing.


def unzip(pairs):
    """
    Splits list of pairs (tuples) into separate lists.

    Example: pairs = [("a", 1), ("b", 2)] --> ["a", "b"] and [1, 2]

    """
    return tuple(zip(*pairs))


def get_entities(sentence):
    """
    Gets the entities from a sentence.

    params:
        sentence[str]:
            The sentence that you want to get the proper nouns of.

    returns:
        proper_nouns[list of list of tuples]:
            A list of list of tuples that has the proper nouns and their part of speech.
            ie.
            [[('North', 'NNP'), ('Korea', 'NNP')],
            [('Kim', 'NNP'), ('Jong', 'NNP'), ('Un', 'NNP')],
            [('US', 'NNP')],
            [('Dennis', 'NNP'), ('Rodman', 'NNP')]]

    """

    tokens = word_tokenize(sentence)
    pos = nltk.pos_tag(tokens)
    named_entities = nltk.ne_chunk(pos, binary=True)
    proper_nouns = []
    for i in range(0, len(named_entities)):
        ents = named_entities.pop()
        if getattr(ents, 'label', None) != None and ents.label() == "NE":
            proper_nouns.append([ne for ne in ents])

    return proper_nouns


def most_associated_with_entity(search_engine, entity, num_entities=10, num_docs=10):
    """
    Gets the entities that are associated with another entity.

    params:
        search_engine [MySearchEngine]:
            The search engine

        entity[string]:
            The entity that you want to find the entities associated with it.

        num_entities[int]:
            An int that describes the amount of entities returned.

        num_docs[int]:
            An int that describes the amount of docs that are wanted to be looked at.

    returns:
        associated_entities[Iterable]:
            The top num_entities entities associated with the asked for entity.

    """

    queries = search_engine.query(entity, k=num_docs)
    docs, scores = unzip(queries)
    associated_entities = []
    b = []
    for doc in docs:
        a = get_entities(search_engine.get(doc))
        for list1 in a:
            entities, part_of_speech = unzip(list1)
            b.append(" ".join(entities))

    for i in b:
        if i not in associated_entities:
            associated_entities.append(i)

    return associated_entities[:num_entities]
