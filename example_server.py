import random, copy
from helper import Helper

#Original Generate without using our library
def generate(data):

    # Sample two random integers between 5 and 10 (inclusive)
    a = random.randint(5, 10)
    b = random.randint(5, 10)

    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b

    # Compute the sum of these two integers
    c = a + b

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c

#After using our library
def generate(data):

    helper_class = Helper([(5,10), (7,11), (1,4)])
    variant_number = 5

    a, b, c = helper_class.generate_values(variant_number)
    
    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b

    # Compute the sum of these two integers
    c = a + b

    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c


check = Helper([(5,10), (7,11), (1,4)])
for i in range(60):
    print(i, check.generate_values(i))