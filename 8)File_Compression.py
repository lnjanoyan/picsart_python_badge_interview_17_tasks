# inp = r"C:\Users\Admin\Desktop\m.txt"
# out = r"C:\Users\Admin\Desktop\res.txt"
inp = input('Enter your input file path: ')
if inp.startswith("'") or inp.startswith('"'):
    inp = inp[1:-1]

out = input('Enter output file path: ')
if out.startswith('"') or out.startswith("'"):
    out = out[1:-1]
try:
    open(inp)
    open(out)

except FileNotFoundError:
    print('File not found!')
else:
    fin = open(inp)
    fot = open(out, 'w')
    count = 1
    rep = False
    for line in fin:
        for index in range(len(line) - 1):

            if line[index] == line[index + 1]:
                rep = True
                count += 1
            elif rep:
                fot.write(line[index] + str(count))
                rep = False
                count = 1
            else:
                # res = False
                fot.write(line[index])
                count = 1
        fot.write('\n')
    fin.close()
    fot.close()
