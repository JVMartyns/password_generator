import generate_password as gp

if __name__ == '__main__':
    length = int(input('number of characters: '))
    print(gp.generate_password(length))
