import random

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
lowercase = alphabet.split(",")
uppercase = alphabet.upper().split(",")
numbers = '0,1,2,3,4,5,6,7,8,9'.split(",")
special_characters = '!,@,#,$,%,&,?'.split(",")


def generate_password(length):
    while True:
        password = __generator(length)
        if __good_password(password):
            break
    return password


def __generator(length):
    global lowercase, uppercase, numbers, special_characters
    password = ''
    while len(password) < length:
        selected_list = random.choice([lowercase, uppercase, numbers, special_characters])
        character = str(random.choice(selected_list))
        password += character
    return password


def __good_password(password):
    global lowercase, uppercase, numbers, special_characters
    has_lowercase = has_uppercase = has_numbers = has_special_characters = False

    for character in password:
        if character in lowercase:
            has_lowercase = True
            break

    for character in password:
        if character in uppercase:
            has_uppercase = True
            break

    for character in password:
        if character in numbers:
            has_numbers = True
            break

    for character in password:
        if character in alphabet:
            has_special_characters = True
            break

    if has_lowercase and has_uppercase and has_numbers and has_special_characters:
        return True
    else:
        return False
