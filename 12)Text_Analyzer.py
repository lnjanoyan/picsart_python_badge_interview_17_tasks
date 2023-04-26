def sent_cnt():
    count = 0
    for i in f.read():
        if i == '.' or i == '?' or i == '!' or i == ':':
            count += 1
    st = 'The number of sentences is %i' % count
    res.write(st, '\n')


def let_cnt():
    count = 0
    for line in f:
        for char in line:
            if char.isalpha():
                count += 1
    st = 'The number of letters is %i' % count
    res.write(st, '\n')


def word_cnt():
    count = 0
    for line in f:
        if line == '\n':
            continue
        for char in line:
            if char == ' ' or char == '\n' or char == '.' or char == '!' \
                    or char == ',' or char == ':' or char == '(' \
                    or char == '\t' or char == ')' or char == '?':
                count += 1
                if char == '\n':
                    continue
    st = 'The number of words is %i ' % count
    res.write(st, '\n')


def freq_let():
    text = f.read()
    most = '-'
    most_cnt = 0
    for i in text:
        if i.isalpha() and text.count(i) > most_cnt:
            most = i
            most_cnt = text.count(i)
    if most_cnt == 0:
        res.write('No frequent letter\n')
    else:
        st = 'The most used letter in a text is - {}. Its count is {}'.format(most, most_cnt)
        res.write(st, '\n')


def freq_word():
    text = f.read()
    f.seek(0)
    most_cnt = 0
    for line in f:
        start = 0
        if line == '\n':
            continue
        for char in range(len(line)):
            if line[char] == ' ' or line[char] == '\n' or line[char] == '.' or line[char] == ',' or \
                    line[char] == ':' or line[char] == '?' or line[char] == '    ' or line[char] == '!':
                word = line[start:char]
                if text.count(word) > most_cnt and word != '' and len(word) > 1:
                    most_word = word
                    f.seek(0)
                    most_cnt = text.count(word)
                if line[char] == '\n':
                    continue
                else:
                    start = char + 1
    st = 'The most frequent word is {} and its count = {}'.format(most_word, most_cnt)
    res.write(st, '\n')


# main program
inp = input('Enter file path to analyze it: ')
res = open(r"C:\Users\Admin\Desktop\res.txt", 'a')
# inp = r"C:\Users\Admin\Desktop\n.txt" -ready option,for not finding file
if inp.startswith('"') or inp.startswith("'"):
    inp = inp[1:-1]
try:
    open(inp)
except FileNotFoundError:
    print('File not found')
else:
    print('Welcome to text analyzer')
    while True:
        f = open(inp)
        print('\nThere are 5 options for analysis\n1 - Word count\n2 - Letter '
              'count\n3 - Sentence count\n4 - Most frequent letter\n5 - Most frequent word\n6 - End program\n')
        opt = input('Type one of these numbers: ')
        if opt == '1':
            word_cnt()
        elif opt == '2':
            let_cnt()
        elif opt == '3':
            sent_cnt()
        elif opt == '4':
            freq_let()
        elif opt == '5':
            freq_word()
        elif opt == '6':
            print('Program ended!')
            break
        else:
            print('Please type only one of these numbers.\n')

res.close()
