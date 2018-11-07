# Avoid using start, end, and stride in a single slice


def main():
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print(f'Every other {a[::2]}')
    print(f'Every other from second {a[1::2]}')
    print(f'Every other from second not including last one {a[1:-1:2]}')


if __name__ == '__main__':
    main()
