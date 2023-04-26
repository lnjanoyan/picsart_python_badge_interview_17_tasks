def line_count():
    count = 0
    for line in f:
        count += 1
    return count


def chr_count():
    count = 0
    for line in f:
        for char in line:
            if char != '\n':
                count += 1
    return count


def word_count():
    count = 0
    for line in f:
        if line == '\n':
            continue
        for char in line:
            if char == ' ' or char == '\n' or char == '.' or \
                    char == ',' or char == ':' or char == ')' or char == '(' \
                    or char == '    ' or char == '?' or char == '!':
                count += 1
    return count


def word_search():
    word = input('Type searching word: ')
    print('Line(s) of searching word is(are):')
    line_num = 1
    for line in f:
        if word in line:
            print(line_num, line)
        line_num += 1


def freq_word():
    f = open(r"C:\Users\Admin\Desktop\n.txt")
    text = f.read()
    f.seek(0)
    most_cnt = 0
    for line in f:
        start = 0
        if line == '\n':
            continue
        for char in range(len(line)):
            if line[char] == ' ' or line[char] == '\n' or line[char] == '.' or line[char] == ',' or \
                    line[char] == ':' or line[char] == '?' or line[char] == '    ' or line[char] == '!' \
                    or line[char] == '(' or line[char] == ')':
                word = line[start:char]
                if text.count(word) > most_cnt and word != '' and len(word) > 1:
                    most_word = word
                    f.seek(0)
                    most_cnt = text.count(word)
                if line[char] == '\n':
                    continue
                else:
                    start = char + 1
    print('The most frequent word is {} and its count = {}'.format(most_word, most_cnt))


inp = input('Enter file path to analyze it: ')
# inp = r"C:\Users\Admin\Desktop\n.txt"
if inp.startswith('"') or inp.startswith("'"):
    inp = inp[1:-1]
try:
    open(inp)
except FileNotFoundError:
    print('File not found')
else:
    while True:
        f = open(inp)
        print(
            '\nThere are 5 options for analysis\n1 - Word count\n2 - Character count\n3 - Line '
            'count\n4 - Most frequent word\n5 - Word search\n6 - End analysis\n')
        opt = input('Type one of these numbers: ')
        if opt == '1':
            print('Words count is ', word_count())
        elif opt == '2':
            print('Characters count is ', chr_count())
        elif opt == '3':
            print('Lines count is ', line_count())
        elif opt == '4':
            print(freq_word())
        elif opt == '5':
            word_search()
        elif opt == '6':
            print('Program ended!')
            break
        else:
            print('Please type only one of these numbers.\n')
