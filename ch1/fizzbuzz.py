# 3 fizz, 5 buzz, 3*5 fizzbuzz

for i in range(1, 101):
    if i%15 == 0: print("fizzbuzz")
    elif i%3 == 0: print("fizz")
    elif i%5 == 0: print("buzz")
    else:
        print(i)