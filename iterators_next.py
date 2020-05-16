

import itertools

#region
# my_list = list("abcdefghij")
# indexes = itertools.count(start=0, step=1)
# for i, c in zip(indexes, my_list):
#     print(i, c)


# for i in itertools.count(4, 0.5):
#     print(i)

# for x in itertools.cycle(["Python", "is", "wonderful"]):
#     print(x)

# for x in itertools.repeat("Hi"):
#     print(x)


def deck():
    suits = ["Clubs"]#, "Spades", "Hearts", "Diamonds"]
    numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
    yield from itertools.product(suits, numbers)


# count = 0
# for cards in itertools.permutations(deck()):
#     count += 1
#     if count % 100000 == 0:
#         print(f"Calculated {count}")




# for n, suit in deck():
#     print("{} of {}".format(n, suit))


# hearts = [(n, suit) for n, suit in deck() if suit == "Hearts"]
# for cards in itertools.combinations(hearts, 2):
#     for n, suit in cards:
#         print("{} of {}".format(n, suit), end=", ")
#     print()


# x_coords = range(0, 4)
# y_coords = range(0, 4)

# for x in x_coords:
#     for y in y_coords:
#         print(x, y)

# for x, y in itertools.product(x_coords, y_coords):
#     print(x, y)

#endregion


# friends = ["Alice", "Bob", "Charlie", "Dominic", "Eugene"]
# for a, b, c in itertools.combinations(friends, 3):
#     print(a, b, c)


# largest = 0
# for n in numbers:
#     if n > largest:
#         largest = n
# print(largest)

# def average(*iterable):
#     return sum(iterable) / len(iterable)

# x = [2,4,6,8,67,4,3,6,84,3,31]
# for n in itertools.accumulate(x, average):
#     print(n)



# itertools.tee()


cards = list(deck())
print(cards)
print(cards)
print(cards)
print(cards)
print(cards)

cards1, cards2 = itertools.tee(cards, 2)

def print_cards(cards):
    print("---- Beginning print")
    for card in cards:
        print("{} of {}".format(*card))
    print("---- Finishing print")

print_cards(cards1)
cards1 = deck()
print_cards(cards1)



# cards = deck()
# for c in cards[10:20:3]:
#     print(c)
# for c in itertools.islice(cards, 10, 20, 3):
#     print(c)



# itertools.islice()


