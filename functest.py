def lesser_of_two_evens(a,b):
    if(a%2==0 and b%2==0):
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    sliced_text = text.split(" ")
    if (sliced_text[0][0].lower() == sliced_text[1][0].lower()):
        return True
    else:
        return False

print(animal_crackers("Levelheasded Llama"))
print(animal_crackers("Crazy Kangaroo"))

def makes_twenty(n1,n2):
    if(n1+n2==20):
        return True
    elif(n1==20 or n2==20):
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(5,15))
print(makes_twenty(2,3))

def old_macdonald(name):
    new_name = ""
    for i in range(len(name)):
        if (i==0 or i==3):
            new_name = new_name + name[i].upper()
        else:
            new_name = new_name + name[i]
    return new_name

print(old_macdonald('macdonald'))

def master_yoda(text):
    splited_text = text.split(" ")
    splited_text.reverse()
    return " ".join(splited_text)
    

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

def almost_there(n):
    if (n-100>=-10 and n-100<=10):
        return True
    elif (n-200>=-10 and n-200<=10):
        return True
    else:
        return False

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

def has_33(nums):
    for i in range(len(nums)):
        if (nums[i] == 3 and i != len(nums)-1):
            if(nums[i+1] == 3):
                return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3, 3]))

def paper_doll(text):
    return_text = ""
    for i in range(len(text)):
        for j in range(0,3):
            return_text = return_text + text[i]
    return return_text

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

def blackjack(a,b,c):
    sum_num = a+b+c
    if(sum_num <= 21):
        return sum_num
    else:
        if 11 in [a,b,c] and sum_num-10 <= 21:
            return sum_num-10
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

def summer_69(arr):
    result = 0
    sum_possible = True
    for i in range(len(arr)):
        if arr[i] == 6:
            sum_possible = False
        if arr[i] == 9:
            sum_possible = True
            continue
        if sum_possible:
            result = result + arr[i]
    return result

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
