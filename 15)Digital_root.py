while True:
    try:
        num = int(input('Enter a positive integer number(example: 145688): '))
    except ValueError:
        print('Please type only POSITIVE INTEGER number! (example: 7813)')
    else:
        if num < 0:
            print('Negative number!!! Please type non negative integer')
            continue
        summ = 0
        while num > 9:
            summ = 0
            for i in str(num):
                summ += int(i)
            num = summ
        print('Digital root = ', num)
