#Task 1 - printing single object
#Your task is to print values of primitive data types, 
#one type in one line. Use following types: integer, float, complex, string, boolean

a = 5
b = 2.2254 
c = 'hey'
d = True
f = (4+1j)
# intdeger
print('a=',a)
# float
print('b=',b)
#complex
print(f)
#string
print(c)
#boolean
print(d)

#Task 2 - printing type of given value
#Your task is to print two objects with separator for the same primitive types as in task 1.
#The first object is a value of given type, the second object is a type of value.
#The separator is a string " is type of ".





#task 3 checking type of value (version 2)
#Your task is a slightly modification of task 3. 
# Instead printing True or False modify your code to get readable information 
# about the type of your value.
result_1=isinstance(b,int)
print('b is instance of integer ', result_1)

result_2=isinstance(c, str)
print('c is instance of integer ', result_2)

result_3=isinstance(c,int)
print('c is instance of integer ', result_2)


