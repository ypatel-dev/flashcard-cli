# Yesha Patel
# Nov 1, 2026
import json
import random
import sys

def load_flashcards(filename):
    """Load flashcards from a JSON file and return a list of cards."""
    with open(filename, encoding='utf-8') as file:
        flashcards = json.load(file)
        return flashcards

def run_quiz(flashcards):
    """Ask each flashcard question and check the user's answer."""
    score = 0
    deck = flashcards[:]
    random.shuffle(deck)  # Shuffle the deck to randomize question order
    for card in deck:
        print("\n" + card['question'])
        user_answer = input("Your answer: ")

        if user_answer.strip().lower() == card['answer'].strip().lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    print(f"Your final score is: {score}/{len(deck)}")
    return score

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'cards.json'
    flashcards = load_flashcards(path)
    run_quiz(flashcards)

if __name__ == "__main__":
    main()