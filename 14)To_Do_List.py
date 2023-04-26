import json


def add():
    task = input('Enter a new task:(Task must be only ONE sentence:  ')
    dot = task.count('.')
    ques = task.count('?')
    ex = task.count('!')
    if (dot and not ques and not ex) or (not dot and ques and not ex) or \
            (not dot and not ques and ex) or (not dot and not ex and not ques):
        if task in tasks:
            print('Task is already exists, you can delete or mark it as done \n')
        else:
            global number
            number += 1
            status = '-'
            content = [number, task, status]
            tasks.append(content)
            print('\nAdded!\n')
    else:
        print('Task must be one sentence!!!')

    with open(path, 'w') as f:
        json.dump(tasks, f)


def mark_done():
    try:
        mark_num = int(input('Enter task number for removing: '))
    except ValueError:
        print('Number not founded!')
    else:
        for i in range(len(tasks)):
            if mark_num == tasks[i][0]:
                tasks[i][2] = "Done"
                with open(path, 'w') as f:
                    json.dump(tasks, f)
                print('Marked\n')
                break

        else:
            print('No such contact\n')


def remove():
    try:
        del_task_num = int(input('Enter task number for removing: '))
    except ValueError:
        print('Number not founded!')
    else:
        for i in range(len(tasks)):
            if del_task_num == tasks[i][0]:
                del tasks[i]
                with open(path, 'w') as f:
                    json.dump(tasks, f)
                print('Deleted\n')
                break

        else:
            print('No such contact\n')


def read():
    with open(path, 'r') as f:
        data = json.load(f)
    print(data)


tasks = []
number = 0
path = r"C:\Users\Admin\Desktop\tasks.json"
print('This is your todo list.')
while True:
    # f = open(r'C:\Users\Admin\Desktop\tasks.json', 'w')
    inp = input('Type one of these options\n\n1 - For adding new task\n2 - For marking task is done \n3 - For'
                ' removing task \n4 - For reading all tasks\n5 - For ending program\n\nYour answer: ')

    if inp == '1':
        add()
    elif inp == '2':
        pass
        mark_done()
    elif inp == '3':
        remove()
    elif inp == '4':
        read()
    elif inp == '5':
        break
    else:
        print("\n!!!!Please enter one of the suggesting numbers.")
