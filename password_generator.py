def _main():
    print(generate_password())


def generate_password(length: int = 14) -> str:
    """Generates a strong password"""
    from random import choice, choices, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    if length < 14:
        raise ValueError('Choose bigger length')
    password = choices(ascii_uppercase + ascii_lowercase + digits +
                       punctuation, k=length-4)
    required = list(map(choice, (ascii_uppercase, ascii_lowercase, digits,
                                 punctuation)))
    shuffle(required)
    for i in sorted(choices(range(length - 3), k=4), reverse=True):
        password.insert(i, required.pop())
    return ''.join(password)


if __name__ == '__main__':
    _main()
