# wumpus_population.py
# We can use loops to simulate natural processes over time. Write a program that calculates the 
# populations of two kinds of “wumpuses” over time. At the beginning of year 1, there are 1000 slow 
# wumpuses and 1 fast wumpus. This one fast wumpus is a new mutation. Not surprisingly, being fast 
# gives it an advantage, as it can better escape from predators. Each year, each wumpus has one 
# offspring. (We'll ignore the more realistic niceties of sexual reproduction, like distinguishing 
# males and females.). There are no further mutations, so slow wumpuses beget slow wumpuses, and fast
 # wumpuses beget fast wumpuses. Also, each year 40% of all slow wumpuses die each year, while only 
 # 30% of the fast wumpuses do.

# So, at the beginning of year one there are 1000 slow wumpuses. Another 1000 slow wumpuses are born.
# But, 40% of these 2000 slow wumpuses die, leaving a total of 1200 at the end of year one. Meanwhile,
# in the same year, we begin with 1 fast wumpus, 1 more is born, and 30% of these die, leaving 1.4. 
# (We'll also allow fractional populations, for simplicity.)

# Beginning of Year	Slow Wumpuses	Fast Wumpuses
        # 1	            1000	        1
        # 2	            1200	        1.4
        # 3	            1440	        1.96
        # …	            …	            …
# Enter the first year in which the fast wumpuses outnumber the slow wumpuses. Remember that the table
# above shows the populations at the start of the year
i = 1
slow = 1000.0
fast = 1.0

print i, slow, fast

while fast < slow:
    i += 1
    slow = (slow * 2) - ((slow * 2) * (40.0 / 100.0))
    fast = (fast * 2) - ((fast * 2) * (30.0 / 100.0))
    print i, slow, fast
    
# card_center.py
# What is the position of the center of the top-left card (Ace of Clubs, A♣) in the tiled image 
# discussed in the "Tiled images" video? Remember that each card in this tiled image has size 
# 73 x 98 pixels.

# What is the position of the center of the bottom-right card (King of Diamonds, K♦) in the tiled 
# image discussed in the "Tiled images" video? Again, remember that each card in this tiled image has
# size 73 x 98 pixels.
CARD_WIDTH  = 73
CARD_HEIGHT = 98

def card_center(ROW, COL):
    x = (CARD_WIDTH  * COL) - (CARD_WIDTH  / 2.0)
    y = (CARD_HEIGHT * ROW) - (CARD_HEIGHT / 2.0)
    return x, y
    
    
# while_len.py
# Convert the following English description into code.

# 1 . Initialize n to be 1000. Initialize numbers to be a list of numbers from 2 to n, but not including n.
# 2. With results starting as the empty list, repeat the following as long as numbers contains any numbers.
        # Add the first number in numbers to the end of results.
        # Remove every number in numbers that is evenly divisible by (has no remainder when divided by) 
            # the number that you had just added to results.
# How long is results?

# To test your code, when n is instead 100, the length of results is 25.

n = 1000
numbers = range(2, n)
results = []
while len(numbers) > 0:
    num_list = numbers[:]
    divisor = numbers[0]
    results.append(divisor)
    for number in numbers:
        if number % divisor == 0:
            num_list.remove(number)
    numbers = num_list[:]
print len(results)