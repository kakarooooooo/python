myfile = open('myfile.txt')
# myfile = open('wrongfile.txt')

print(myfile.read())
print(myfile.read())

myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readlines())

myfile.close()

with open('myfile.txt', mode='r') as my_new_file:
    contents = my_new_file.read()

print('contexts' + contents)

with open('my_new_file.txt', mode="a") as new_file:
    new_file.write("\nFOUR ON FOURTH")
    

with open('my_new_file.txt', mode="r") as new_file:
    print(new_file.read())