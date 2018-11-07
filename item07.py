# Use list comprehensions instead of map and filter


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    squared = [x**2 for x in a]
    print(f'squared {squared}')

    squared_even = [x**2 for x in a if x % 2 == 0]
    print(f'squared even {squared_even}')

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [x for row in matrix for x in row]
    print(f'flattened {flattened}')

    matrix_squared = [[x**2 for x in row] for row in matrix]
    print(f'squared matrix {matrix_squared}')


if __name__ == '__main__':
    main()
