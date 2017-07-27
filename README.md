# News_Buddy

entity: Any proper noun


1. What's new with "movies"?

  --> 1st sentence of highest ranking document
  ```
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
  ```
 
2. Top entity associated with [Kim K]:

  --> [Chris Jenner, ...]
  
  ```
  def most_associated_with_entity(search_engine, entity, k=10):
    """
    Gets the entities that are associated with another entity.

    param:
        search_engine [MySearchEngine]:
            The search engine

        entity[string]:
            The entity that you want to find the entities associated with it.

        k[int]:
            An int that describes the amount of entities returned.

    returns:
        associated_entities[Iterable]:
            The top k entities associated with the asked for entity.
    """
  ```
  
3. Top entities associated with "sports":

  --> [Boston, Boston Red Sox,...]
  
  ```
  def most_associated_with_phrase(search_engine, phrase):
  
      """
      Gets the entities that are associated with a word/topic/phrase. 
      
      param:
        search_engine [MySearchEngine]:
          The search engine
          
        word[str]:
          The word/phrase that you want to find the entities associated with it. 
          
       returns:
         associated_entities[Iterable]:
            The entities associated with the asked for word. 
        """          
  ```

