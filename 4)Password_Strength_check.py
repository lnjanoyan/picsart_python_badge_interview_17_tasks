f = open(r"C:\Users\Admin\Desktop\banned_words.txt")
inp = input('Enter your password: ')
inp = inp.replace(' ', '')
if len(inp) >= 8:
    if inp.lower() != inp:
        if inp.upper() != inp:
            if not inp.isalnum():
                for i in inp:
                    if i.isdigit():
                        for line in f:
                            if line[:-1] in inp:
                                print("Password cannot contain dictionary words")
                                break
                        else:
                            print('Strong password')
                            break
                else:
                    print('Password must contain at least one number')
            else:
                print('Password must contain special characters')
        else:
            print('Password must contain at least one lowercase character')
    else:
        print('Password must contain at least one uppercase character')
else:
    print('Password length must be min 8 characters.')
