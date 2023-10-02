import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self, path):
        """Read file and returns number of items read"""
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Parse through the file for list of words"""
        return [word.strip() for word in file]
    
    def random(self):
        """return a random word"""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    def parse(self, file):
        """Parse file for list of words, skipping blank lines or comments."""
        return [word.strip() for word in file
            if word.strip() and not word.startswith("#")]