# Prefer enumerate over range


def main():
    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

    # enumerate returns index and item
    for i, f in enumerate(flavor_list):
        print(f'Item {i} is {f}')

    # enumerate returns a generator
    x = enumerate(flavor_list)
    print(f'{next(x)}')
    print(f'{next(x)}')

    for i, f in x:
        print(f'Item {i} is {f}')  # starts at index 2


if __name__ == '__main__':
    main()
