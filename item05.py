# Know how to slice sequences


def main():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(f'First four {a[:4]}')
    print(f'Last four {a[-4:]}')
    print(f'Middle two {a[3:-3]}')

    # slicing returns a (shallow) copy
    b = a[4:]
    print('Before: ', b)
    b[1] = 99
    print('After: ', b)
    print('No change:', a)


if __name__ == '__main__':
    main()
