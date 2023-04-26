import json


def add():
    name = input('Please enter name for a new contact: ')
    surname = input('Enter surname: ')
    phone = input('Enter phone number: ')
    address = input('Enter address: ')
    if name in contacts:
        print('Contact with name {} is already exists, you can delete or edit that one\n'.format(name))
        return False
    info = dict(surname=surname, phone=phone, address=address)
    contacts[name] = info
    with open(path, 'w') as f:
        json.dump(contacts, f)
    return '\nAdded!\n'


def edit():
    editing_contact = input('Enter contact name for editing: ')
    if editing_contact in contacts:
        field = input('Enter field for editing: surname - phone - address:  ')
        if field in contacts[editing_contact]:
            new_value = input("Enter new {} ".format(field))
            if new_value is not None:
                contacts[editing_contact][field] = new_value
            else:
                contacts[editing_contact][field] = ''

        else:
            print('No such field in phonebook! ')
        with open(path, 'w') as f:
            json.dump(contacts, f)
        print('Edited!\n')
    else:
        print("No such contact in phonebook!\n")


def remove():
    deleting_contact = input('Enter contact name for removing: ')
    if deleting_contact in contacts:
        del deleting_contact
        with open(path, 'w') as f:
            json.dump(contacts, f)
        print('Deleted\n')
    else:
        print('No such contact\n')


def read():
    with open(path, 'r') as f:
        data = json.load(f)
    print(data)


contacts = {}
path = r"C:\Users\Admin\Desktop\phonebook.json"
while True:
    inp = input('For adding a contact type "add". \nFor editing an information type "edit". \nFor'
                'removing a contact type "remove". \nFor ending type "end". \nFor reading all information type '
                '"read". \nYour answer: ')

    if inp == 'add' or inp == 'ADD' or inp == 'Add':
        print(add())
    elif inp == 'edit' or inp == 'Edit' or inp == 'EDIT':
        edit()
    elif inp == 'remove' or inp == 'REMOVE' or inp == 'Remove':
        remove()
    elif inp == 'read' or inp == 'READ' or inp == 'Read':
        read()
    elif inp == 'end' or inp == 'End' or inp == 'END':
        break
    else:
        print("\n!!!!Please enter one of the suggesting commands: add - edit - remove - end\n ")
