while True:
    f = open(r"C:\Users\Admin\Desktop\crossword_cheater.txt")
    inp = input('Enter a word with the letters you know filled in and asterisks for'
                ' those you don’t know,(For end the program type 0): ')
    if inp == '0':
        break
    for i in inp:
        if (not i.isalpha()) and i != '*':
            print('Different character found.Please use only letters and * ')
            break
    else:
        for line in f:
            line = line[:-1]
            if len(line) == len(inp):
                for index in range(len(line)):
                    if inp[index] != line[index] and inp[index] != '*':
                        break
                else:
                    print(line)
            else:
                continue
