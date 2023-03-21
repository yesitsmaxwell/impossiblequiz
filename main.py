number = 1
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
