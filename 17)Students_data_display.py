f1 = open(r"C:\Users\Admin\Desktop\students.txt")
f2 = open(r"C:\Users\Admin\Desktop\students2.txt", 'w')
for line in f1:
    ls = line.split()
    ls[0] = ls[0].title()
    ls[1] = ls[1].title()
    ls[3] = '301-' + ls[3]
    for i in range(len(ls)):
        f2.write(ls[i])
        f2.write('\t')
    f2.write('\n')
f2.close()
f2 = open(r"C:\Users\Admin\Desktop\students2.txt")
print(f2.read())
