

is_running_outer = True

tasks = []



while is_running_outer:
    
    print('===== TO DO LIST =====')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Remove Task')
    print('4. Exit')

    choosed = int(input('Choose: '))

    if choosed == 1:

        is_running = True
        print('Enter Done to end the program: ')
        while is_running:
            task = input('Enter a Task: ')
            if task == 'done' or task == 'Done':
                break
            tasks.append(task)
        print(tasks)
        print('')

    elif choosed == 2:

        print('')
        if len(tasks) == 0:
            print('No Tasks Available.')
        else:
            for index, task in enumerate(tasks, start=1):
                print(f'{index}. {task}')
        print('')

    elif choosed == 3:

        if len(tasks) == 0:
            print('No Tasks Available.')
        else:
            for index, task in enumerate(tasks, start=1):
                print(f'{index}. {task}')
        task_to_remove = int(input('Enter task number to remove: '))
        tasks.pop(task_to_remove - 1)
        print('')

    elif choosed == 4:

        is_running_outer = False
        print('Thank You! See you soon')

