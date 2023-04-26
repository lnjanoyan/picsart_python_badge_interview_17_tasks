import random

f = open(r"C:\Users\Admin\Desktop\words.txt")
while True:
    inp = input('Enter an acronym: ').replace(' ', '')
    ls = []
    if inp.isalpha():
        low = inp.lower()
        for i in low:
            f.seek(0)
            ls.append(random.choice([line[:-1] for line in f if line.startswith(i)]))
        print(ls)

    else:
        print('Please type only letters')
