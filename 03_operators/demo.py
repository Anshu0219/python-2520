num1 = 100
num2 = 25
print(f"sum of {num1} and {num2} is {num1+num2}")
print(f"difference of {num1} and {num2} is {num1-num2}")
print(f"mulitiple of {num1} and {num2} is {num1*num2}")
print(f"division of {num1} and {num2} is {num1/num2}")
print(f"modulu of {num1} and {num2} is {num1%num2}")
x = 20  #assignment
x += 1
print(x)
x -= 3
print(x)
x *= 5
print(x)
x //= 4
print(x)
x /= 1
print(x)
x %= 2
print(x)
x **= 4
print(x)
a = 8   #comparison 
b = 2
print(a==b)
print(a!=b) #!= not equal 
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
a = 11   #logical          
b = 5
print(a and b)     #a and b → both are non-zero (truthy) → returns last value → 5.
print(a or b)      #a or b → first value 11 is already truthy → returns 11.
print(not a)       #not a → a=11 is truthy → so not makes it False.
print(not b)       #not b → b=5 is also truthy → so not makes it False.
a = 4
b = 2  # bitwise
print(a&b)      #And (the result bit is 1 only if both corresponding input bits are 1.)
print(a^b)      # xor (the result bit is 1 only if both corresponding input bits are different)
print(~a)        #-(a+1)
print(a<<b)
print(a>>b)
print(a|b)       #or(The result bit is 1 if at least one corresponding input bit is 1.)
list = [1,2,3,4]
print(5 is not list)    #membership
print(3 is list)
emp_ids = [101,102,103,104,106,107,108,109,110]
print(105 is  emp_ids)
print(101 is  not emp_ids)
x = [3,4,5]
y = x
z = [3,4] #identifier
print(x is y)
print(x is z)
print(x is not z)

