# Take advantage of each block in try/except/else/finally


def main():
    try:
        value = 1 / 0
        print(f'divided by zero value - {value}')
    except ZeroDivisionError as e:
        print(f'divide by zero error - {e}')
    else:
        print('managed to successfully divide by zero!')
    finally:
        print('always called')


if __name__ == '__main__':
    main()
