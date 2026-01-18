import random

friends = ["Alice" , "Bob" , "Charlie" , "David" , "Emanuel"]
# 1 option
print(random.choice(friends))
#2 option
random_index = random.randint(0, 4)
print(friends[random_index])