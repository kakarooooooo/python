def myfunc(*args):
    return sum(args)

print(myfunc(1,2,41,12,1411))

def myfunc2(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no fruit')

myfunc2(fruit='apple', veggie='lettuce')


def myfunc3(my_str):
    return_str = ""
    for i in range(len(my_str)):
        if i%2 != 0:
            return_str = return_str+ my_str[i].upper()
        else:
            return_str = return_str+ my_str[i].lower()
    return return_str

print(myfunc3("AHSAaaaaaaFSDAFAS"))