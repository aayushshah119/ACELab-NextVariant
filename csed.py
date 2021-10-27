from random import sample, shuffle

first_digit = (a for a in sample(range(5,9), 4))
second_digit = (b for b in sample(range(3,9), 6)) 
list_second_digits = []
list_first_digits = []
dicti = {}
index2 = 0
index = 0
def fn1():
    global index
    digit = next(first_digit, None)
    if digit == None:
        temp = index
        index += 1
        return list_first_digits[temp%4]
    else:
        list_first_digits.append(digit)
        return digit

def fn2():
    global index2
    digit = next(second_digit, None)
    if digit == None:
        temp = index2
        index2 += 1
        return list_second_digits[temp%6]
    else:
        list_second_digits.append(digit)
        return digit

def gen():
    first = fn1()
    second = fn2()
    while (first, second) in dicti:
        second = fn2()
    dicti[(first, second)] = 1
    yield (first, second)


for i in range(24):
    x = next(gen())
    print(x)


"""
if __name__ == "__main__":
    while True:
        cli_input = input()
        if cli_input == "":
            break
        if cli_input == 'n':
            print(next(gen()))
"""
