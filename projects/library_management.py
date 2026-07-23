is_running_outer = True

books = []

while is_running_outer:
    print()
    print('Library Management System')

    print()
    print('1. Add Books')
    print('2. View Books')
    print('3. Exit')

    print()
    choosed = int(input('Choose: '))

    if choosed == 1:
        is_running = True
        print()
        print('Enter done when done adding books: ')
        print()
        while is_running:
            book = input('Add a Book: ')
            if book == 'done':
                is_running = False
            books.append(book)
    elif choosed == 2:
        books.pop(-1)
        print()
        for index, book in enumerate(books, start=1):
            print(f'{index}. {book}')
        print()
    elif choosed == 3:
        is_running_outer = False
        print()
        print('Thank You!')
        print('See You Soon')
    else:
        print()
        print('Invalid Choice! Try Again')
