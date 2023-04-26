import json


def changing_in_file():
    f = open(r"C:\Users\Admin\Desktop\library.json", 'w')
    json.dump(library, f)
    f.close()


def add():
    name = input('Enter book name: ')
    author = input('Enter author full name: ')
    date = input('Enter publication date: ')
    for i in library:
        if name in i['name']:
            print('%s is already in library.You can view or remove it.' % name)
            break
    else:
        library.append({'name': name, 'author': author, 'date': date})
        print('\nBook successfully added.\n')
    changing_in_file()


def remove():
    name = input('Enter book name to remove it: ')
    for i in library:
        if i['name'] == name:
            del i
            print('\nBook successfully deleted.\n')
            break
    else:
        print("No such book in library.")
    changing_in_file()


def view():
    with open(r"C:\Users\Admin\Desktop\library.json") as f:
        content = json.load(f)
        print(content)


def sorting():
    library.sort(key=lambda dicts: dicts['name'])
    changing_in_file()
    print('\nSorted.\n')


library = []
print('Welcome to library!')
while True:
    print('What do you want? \n1 - Add Books\n2 - Remove Books\n3 - '
          'View All Books\n4 - Sort Books Alphabetically\n5 - End program   ')
    choice = input("Choose one of these options: ")
    if choice == '1':
        add()
        print(library)
    elif choice == '2':
        remove()
    elif choice == '3':
        view()
    elif choice == '4':
        sorting()
    elif choice == '5':
        print('Program ended.')
        break
    else:
        print('Invalid command,please choose one of these numbers')
