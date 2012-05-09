Elliot - Project specification
==============================

---

Life cycle - New answers added
==============================

1. An answer is created containing:
    - Answer text
    - Questions
- Each _question_ will be parsed and the keywords will be inserted into the _keywords_ collection in MongoDB.
- Each _answer_ will be inserted to the _answers_ collection in MongoDB, together with it's _questions_.

Life cycle - Question asked
===========================

1. The question is de-fuzzed - all extra characters are removed and all words are lower-case.
- All _keywords_ in the input sentence are found.
- A query towards MongoDB is executed. It will search the _keywords_ collection for matching keywords and return all _answer_ ObjectID's.
- All _answers_ will be sentence-compared with the input sentence.
- The best answer will be returned.

Story 1 - Simple question
=========================

Input - Sentence
----------------

    When was Jesus born?

Input - Breakdown
-----------------

| Word         | Type        |
|--------------|-------------|
| **when**     | modifier    |
| **was**      | modifier    |
| **jesus**    | keyword     |
| **born**     | keyword     |
| **?**        | fuzz        |

Answer - Sentences and parsed values
------------------------------------

| Sentence                   | Parsed                     |
|----------------------------|----------------------------|
| When was Jesus born?       | when was jesus born        |
| When were Jesus born?      | when were jesus born       |
| Which year was Jesus born? | which year was jesus born  |

**Keyword summary**

    year jesus born

Database structure
==================

Collection - keywords
---------------------

Collection mapping a keyword to an answer.

    { 'k': 'jesus', 'a': [ 'answer1', 'answer3' ] }

**Indexes**

 - k

Collection - answers
--------------------

Collection containing all answers and their questions.

    { 'qs': [ 'q1', 'q2', 'q3' ], 'a': '' }

**Indexes**

- qs

List of modifiers
=================

- when
- was
- were
- which
- does
- why
- how

List of fuzz words
==================

- is
- are
- the
- or
- these
