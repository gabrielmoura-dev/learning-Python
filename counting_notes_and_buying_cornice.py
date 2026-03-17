'''
Create a program that reads a renovation note and counts how many words are in it. Then, read your budget and the price per cornice piece, 
and calculate how many complete pieces you can afford to buy.
Print the word count first, then the number of pieces you can purchase (remember: only whole pieces!).
'''
note = input() # Read the renovation note
budget = int(input()) # Read the budget
price_per_piece = int(input()) # Read the price per cornice piece
# TODO: Count the number of words in the note
word = note.split()
word_count = len(word)
# TODO: Calculate how many complete pieces you can afford
pieces_can_buy = int(budget / price_per_piece)
# Print the results
print(word_count)
print(pieces_can_buy)
