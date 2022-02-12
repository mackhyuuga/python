while True:
    try:
        age = int(input('what is your age? '))
        print(age)
    except:
        print('please enter a number')
    else:
        print('thank you')
        break
