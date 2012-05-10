"""
Clean up questions
"""

from .definitions import fuzzy_characters
from .conf import settings

def remove_fuzzy_characters(question):
    """
    Remove all fuzzy characters for a given question
    """
    for character in fuzzy_characters.FUZZY_CHARACTERS[settings.LANGUAGE]:
        question = question.replace(character, '')
    
    return question
