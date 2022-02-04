import random

chars = "ABCDEFGHIJKLMNOPQRSTUWVXYZbacdefghijklmnopqrstuwvxyz123456789"


for i in range(100):
    first = ''.join((random.choice(chars) for i in range(6)))
    second = ''.join((random.choice(chars) for i in range(6)))
    third = ''.join((random.choice(chars) for i in range(27)))

    result = first + "." + second + "./" + third


    output = open("tokens.txt", "a")
    output .write(result + "\n")


