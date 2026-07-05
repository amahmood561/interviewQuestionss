''''quora

Word sense disambiguation is the problem of determining which sense a word takes on in a particular setting, if that word has multiple meanings. For example, in the sentence "I went to get money from the bank", bank probably means the place where people deposit money, not the land beside a river or lake.

Suppose you are given a list of meanings for several words, formatted like so:

{
    "word_1": ["meaning one", "meaning two", ...],
    ...
    "word_n": ["meaning one", "meaning two", ...]
}
Given a sentence, most of whose words are contained in the meaning list above, create an algorithm that determines the likely sense of each possibly ambiguous word.''''


import re
from collections import defaultdict

def tokenize(text):
    """
    Tokenizes the input text into lowercase words, removing punctuation.
    """
    return re.findall(r'\b\w+\b', text.lower())

def word_sense_disambiguation(meanings_dict, sentence, window_size=2):
    """
    Disambiguates the meanings of ambiguous words in a sentence based on context.

    :param meanings_dict: Dictionary mapping words to their list of meanings.
    :param sentence: The sentence in which to disambiguate word senses.
    :param window_size: Number of words to consider before and after the target word for context.
    :return: A dictionary mapping each ambiguous word to its selected meaning.
    """
    tokens = tokenize(sentence)
    word_positions = defaultdict(list)

    # Map each word to its positions in the sentence
    for idx, word in enumerate(tokens):
        word_positions[word].append(idx)

    disambiguated = {}

    for word, meanings in meanings_dict.items():
        if len(meanings) <= 1:
            continue  # No ambiguity

        if word not in word_positions:
            continue  # Word not in sentence

        for pos in word_positions[word]:
            # Extract context window
            start = max(pos - window_size, 0)
            end = min(pos + window_size + 1, len(tokens))
            context = tokens[start:pos] + tokens[pos+1:end]

            # Tokenize context
            context_tokens = set(context)

            # Compute overlap for each meaning
            overlap_scores = []
            for meaning in meanings:
                meaning_tokens = set(tokenize(meaning))
                overlap = len(context_tokens.intersection(meaning_tokens))
                overlap_scores.append(overlap)

            # Select the meaning with the highest overlap
            max_overlap = max(overlap_scores)
            if max_overlap == 0:
                selected_meaning = meanings[0]  # Default to first meaning if no overlap
            else:
                # In case of ties, select the first one
                selected_meaning = meanings[overlap_scores.index(max_overlap)]

            disambiguated_key = f"{word} at position {pos}"
            disambiguated[disambiguated_key] = selected_meaning

    return disambiguated

# Example Usage
if __name__ == "__main__":
    meanings = {
        "bank": [
            "the financial institution where people deposit money",
            "the land alongside a river or lake"
        ],
        "bat": [
            "a typically nocturnal mammal capable of flight",
            "a piece of sports equipment used in baseball"
        ]
    }

    sentence = "I went to get money from the bank and watched a bat fly overhead."

    disambiguated_senses = word_sense_disambiguation(meanings, sentence)

    # Display the results
    for key, meaning in disambiguated_senses.items():
        word, pos = key.rsplit(" at position ", 1)
        print(f"Word '{word}' at position {pos}: {meaning}")
