import random
# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random number:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float:", random_float)

# Select a random element from a list
fruits = ["apple", "banana", "orange", "kiwi"]
random_fruit = random.choice(fruits)
print("Random fruit:", random_fruit)

# Shuffle the elements in a list
deck_of_cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(deck_of_cards)
print("Shuffled deck:", deck_of_cards)