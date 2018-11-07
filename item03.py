# Know the difference between bytes, str and unicode


def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


if __name__ == '__main__':
    print(f'string is string  {isinstance(to_str("a string"), str)}')
    print(f'bytes is string  {isinstance(to_bytes("a string"), str)}')
    print(f'string is bytes  {isinstance(to_str("a string"), bytes)}')
    print(f'bytes is bytes  {isinstance(to_bytes("a string"), bytes)}')
