# Extension

Congratulations on solving the puzzle! This extension exercise concerns automating the final step. It is more of a programming exercise than a code-breaking one.



In `tools/helper.py` there is a class, `TextAnalyser` that has been semi-implemented. The aim of this class is to analyse a piece of text and determine how many English words are present in it.

To complete this extension you need to:

* Copy `dictionary.txt` from the `dictionary/` directory into this one.

* Create a `TextAnalyser` object in `bruceforce.py`. 

  ```python
  def solve():
  	...
  	
  	# File path will be different on Windows
  	dictionary_file = 'dictionary.txt' 
  	analyser = helper.TextAnalyser(dictionary_file)
  ```

* Implement `english_words` in `tools/helper.py`

  ```python
  class TextAnalyser:
  	# some functions to initialise the object #
  	def english_words(self, text):
  		# Your code here! #
  ```

* Use the completed method to solve the puzzle automatically in `bruceforce.py`

  ```python
  def solve():
  	...
  	
  	dictionary_file = 'dictionary.txt'
  	analyser = helper.TextAnalyser(dictionary_file)
  	wc = analyser.english_words('HELLOWORLD')
  ```

  