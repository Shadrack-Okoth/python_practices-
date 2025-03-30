#variable naming
a="banana"
#assigning multiple variables 
a,b,c="banana","cake","juice"
print(c)
#unpack a collection 
x=["banana","cake","juice"]
u,t,k=x
print(k)
#global variables 
v="wow"
def myfunc():
    print("Python is "+ v)
myfunc()
#initializing inside myfunc()
def myfunc():
    global y
    y="potato"
    print("Have eaten "+ y)
myfunc()
#type() function - checks the datatype
x="potato"
print(type(x))
#setting specific data type 
x=float(20)
print(x)
#Generating random number 
import random
print(random.randrange(1,10))
#Strings
#Strings are array 
print(a[1])
#string looping using for
for x in a:
    print(x)
#string length 
print(len(a))
#checking string in a txt
txt="I am, playing now"
if "am" in txt:
    print("yea 'am' is present")
#not in txt
if "you" not in txt:
    print("yes 'you' not present")
#slicing strings 
print(a[2:5])#range
print(a[:5])#start
print(a[0:])#end
#modify string 
print(a.upper())
#strip()remove whitespace
#replace string 
print(a.replace("b","c"))
print(txt.split(","))
#f string format 
t=4
m=7
txt1=f"T + M is {t+m}"
print(txt1)
