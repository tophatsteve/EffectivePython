# Write helper functions instead of complex expressions


def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


if __name__ == '__main__':
    values = {"a": [1, 2, 3], "b": [4, 5, 6]}
    print(get_first_int(values, "b"))  # -> 4
    print(get_first_int(values, "c"))  # -> 0
