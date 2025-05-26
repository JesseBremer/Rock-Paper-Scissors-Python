import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
amount_of_friends = len(friends)

random_selector = random.randint(0, amount_of_friends -1)

print(friends[random_selector])
