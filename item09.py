# Use generators for large list comprehensions


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    it = (x**2 for x in a)  # () instead of []

    print(f'{it}')
    print(f'{next(it)}')  # position 0
    print(f'{next(it)}')  # position 1
    print(f'{next(it)}')  # position 2

    # starts at position 3
    for x in it:
        print(f'{x}')

    new_it = (x for x in a)
    squares = ((x, x**2) for x in new_it)

    # calls both generators in step
    print(next(squares))
    print(next(squares))
    print(next(squares))


if __name__ == '__main__':
    main()
