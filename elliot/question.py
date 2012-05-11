"""
Clean up questions
"""

from .definitions import fuzzy_characters, fuzzy_words, modifiers
from .conf import settings

def full_clean(question):
    """
    Clean up a whole question in all aspects
    """
    question = question.lower()
    question = remove_fuzzy_characters(question)
    question = remove_fuzzy_words(question)
    
    return question

def get_question_characteristics(question):
    """
    Returns keywords and modifiers for the given question.
    
    A full clean is REQUIRED before running this. Or else your
    fuzz will be keywords!
    
    Returns
    {
        'modifiers': [],
        'keywords': [],
    }
    """
    ret = { 'modifiers': [], 'keywords': [] }
    for word in question.split():
        if word in modifiers.MODIFIERS[settings.LANGUAGE]:
            ret['modifiers'] += [word]
        else:
            ret['keywords'] += [word]
    
    return ret

def remove_fuzzy_characters(question):
    """
    Remove all fuzzy characters for a given question
    """
    for character in fuzzy_characters.FUZZY_CHARACTERS[settings.LANGUAGE]:
        question = question.replace(character, '')
    
    return question

def remove_fuzzy_words(question):
    """
    Remove all fuzzy words
    """
    sentence = question.split()
    for word in question.split():
        if word in fuzzy_words.FUZZY_WORDS[settings.LANGUAGE]:
            sentence = filter (lambda stripped: stripped != word, sentence)
    
    return ' '.join(sentence)
