# Use zip to process iterators in parallel


def main():
    names = ['Cecilia', 'Lise', 'Marie']
    letters = [len(n) for n in names]

    longest_name = None
    max_letters = 0

    for name, count in zip(names, letters):
        if count > max_letters:
            max_letters = count
            longest_name = name

    print(longest_name)

    print(zip(names, letters))  # its a generator

    x = zip(names, letters)
    print(next(x))


if __name__ == '__main__':
    main()
