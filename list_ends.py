import sys
def input_list():
    number = raw_input('input numbers\n')
    number = map(int,number.split())
    return number


def list_ends(list):
    x =[]
    x.append(list[0])
    x.append(list[len(list)-1])

    return x

x = input_list()
print list_ends(x)


