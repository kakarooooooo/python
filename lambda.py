from math import pi


my_nums=[1,2,3,4,5]

print(list(map(lambda num: num**2, my_nums)))

print(list(filter(lambda num: num%2==0, my_nums)))


def vol(rad):
    return (4*pi*(rad**3))/3

print(vol(2))


def ran_check(num,low,high):
    if (num in range(low, high+1)):
        print (f"{num} is in the range beetween {low} and {high}")
    else:
        print (f"{num} is in outside from beetween {low} and {high}")

ran_check(5,6,7)

def ran_bool(num,low,high):
    return num in range(low, high+1)

print(ran_bool(3,4,10))


def up_low(s):
    uppernum = lownum = 0
    for j in s:
        if(j.isupper()):
            uppernum += 1
        elif(j.islower()):
            lownum += 1
        else:
            pass
    print(f"No. of Upper case characters : {uppernum}\nNo. of Lower case Characters : {lownum}")
 
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


def unique_list(lst):
    return list(set(lst))

returnArr = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(returnArr)
print(type(returnArr))


def multiply(numbers):
    returnNum = 1
    for i in numbers:
        returnNum *= i
    return returnNum

print(multiply([1,2,3,-4]))


def palindrome(s):
    new_str = s.replace(" ", "")
    return (new_str == ''.join(reversed(new_str)))

print(palindrome('helleh'))


import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for i in alphabet:
        if (str1.lower().find(i)+1):
            continue
        else:
            return False
    return True

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("abababababbdfarsdfvawvsadfvawerxzcv"))


