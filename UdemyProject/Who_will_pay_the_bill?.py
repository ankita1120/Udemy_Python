import random
friends = ["Alice" , "Bob" , "Charlie" , "David" , "Eve" , "Frank"]

#  1st Option
random_friends =random.choice(friends)
print(random_friends)
# 2nd Option
random_index = random.randint(0,4)
print(friends[random_index])

