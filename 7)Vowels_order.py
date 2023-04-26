f = open(r"C:\Users\Admin\Desktop\namelist.txt")
for line in f:
    line = line.lower()
    vowels = 'aeiou'
    a = line.find('a')
    e = line.find('e')
    i = line.find('i')
    o = line.find('o')
    u = line.find('u')
    for vow in vowels:
        if vow not in line:
            break
    else:
        for ch in line:
            if ch in vowels:
                if u >= line.find(ch) >= a:
                    if a < e < i < o < u:
                        if line.find(ch, line.find(ch) + 1) - line.find(ch) == 1 or \
                                line.find(ch, line.find(ch) + 1) > u:
                            print(line.title())
                            break

f.close()