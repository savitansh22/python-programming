#string and numeric values can operate together with *.
a,b = 2,3 
txt = "@"
print(a*txt*b)

# string and string can be operate with +.
a,b = "2", 3 
txt="@"
print((a+txt)*b)

#numeric values can operate with all arithmatic operators.
a,b = 2,3
c = 4
print(a+b*c)

#arithmatic expression with integer and flaot will result in float.
a,b = 10, 5.0
c= a*b
print(c)

#result off division operator with two int will be float.
a,b = 1,2
c = a/b
print(c)

#integer division with float and int will give int displayed as float.
a,b = 1.5, 3
c= a//b
print(c, a/b)

#floor gives closest integer, which is lesser than or equal to the float value.
# result of (a//b) is same as floor(a/b).
a,b = 12,5
c= a//b
print(c)

a,b = -12,5
c= a//b
print(c)

a,b = 12,-5
c= a//b 
print(c)

#remainder is negative when denominator is -.
a,b = -5,2
c=a%b
print(c)

a,b = 5,-2
c= a%b
print(c)