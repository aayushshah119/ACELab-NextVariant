from random import sample, shuffle

first_digit = (a for a in sample(range(5,11), 6))
second_digit = (b for b in sample(range(3,9), 6)) 
index = 0
list_second_digit = []
def gen():
    global index
    for _ in range(6):
        digit = next(first_digit)
        for _ in range(6):
            sdigit = next(second_digit, None)
            if sdigit == None:
                temp = index
                index += 1
                sdigit = list_second_digit[temp%6]
            else:
                list_second_digit.append(sdigit)
            yield (digit, sdigit)
        shuffle(list_second_digit) #To shuffle the second parameter.
for i in gen():
    print(i)
        
