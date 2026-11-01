# Yesha Patel
# Nov 1, 2026
import json

def load_flashcards(filename):
    """Load flashcards from a JSON file and return a list of cards."""
    with open(filename, encoding='utf-8') as file:
        flashcards = json.load(file)
        return flashcards

flashcards = load_flashcards('flashcards.json')
print(flashcards)


