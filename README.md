# News_Buddy

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
  
3. Top entities associated with "sports":

  --> [Boston, Boston Red Sox,...]
