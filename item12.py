# Avoid else blocks after for and while Loops


def main():
    for x in []:
        print('Never runs')
    else:
        print('For else block 1')

    for x in [1]:
        print('Runs once')
    else:
        print('For else block 2')

    while False:
        print('Never runs')
    else:
        print('While else block 1')

    x = 0
    while x < 1:
        print('Runs once')
        x = 1
    else:
        print('While else block 2')


if __name__ == '__main__':
    main()
