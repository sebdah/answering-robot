#!/usr/bin/env python

"""
Testing script
"""

from elliot import question

q = "When was Jesus born?"

print question.get_question_characteristics(question.full_clean(q))
