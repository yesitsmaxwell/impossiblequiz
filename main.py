import random
numberoptions = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
number = (random.choice(numberoptions))
while True:
    print('What is')
    print(number)
    print('plus')
    print(number)
    answer = input('Answer: ')
    answerinteger = int(answer)
    if answerinteger == number * 2:
        print('Well done! You got it right!')
        number = answerinteger
    else:
        print("You got it wrong. Let's try that again...")
        number = 1
