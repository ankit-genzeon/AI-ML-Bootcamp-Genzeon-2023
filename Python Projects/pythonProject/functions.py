#functions
#user-defined
def greet(name):
    '''this greets a person'''
    print("Hello \t"+name+"\t Good Morning")
greet("SRK")

#default

def A(a,b=1,c=2):
    return a+b+c
print(A(3))
print(A(4,4,4))
print(A(2,2))

#keyword
def A(a,b=1,c=2):
 return a+b+c
print(A(a=2,b=3))
print(A(c=3,b=2,a=1))

#positional
def add(a,b,c):
    return a+b+c
print(add(10,20,30))

#arbitary keyword
def key_args(**kwargs):
    return kwargs
my_dict=key_args(Apples=10, Bananaa=20, Chiku=30)
print(my_dict['Apples'])
print(my_dict)

#arbitary positional
def add_num(*n):
    print(n)
    print(sum(n))
add_num(1,2,3,4,5,6)

#higher order function
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def explain (func):
    greet= func("Hi I am Higher Order FuncTIons")
    print(greet)

explain(shout)
explain(whisper)

#lambda
def incr(x):
    x=x+1
    return x
print(incr(4))

print((lambda x:x+1)(4))

res = lambda x:x+1
print(res(4))

print((lambda x,y:x**y)(2,2))

li=[1,2,3,4,5]
def inc(num):
    return num+2
res_list = list(map(inc,li))
print((res_list))

print(list(map(lambda x:x+2,li)))


def eor(num):
    if num%2==0:
        return  "the number {} is even".format(num)
    else:
        return  "the number {} is odd".format((num))

l= [1,2,3,4,5,6,7,8,9,10]
list(map(eor,l))

l4=["apples", "bananan", "chikus"]
r= list(map(lambda x:x.capitalize(),l4))
print(r)

#filter
def odd_num(n):
 if n%2!=0:
   return n
myl=[7,6,7,89,3,2,15]
print (list (filter (odd_num, myl)))

l6=[7, 8, 578, 728, 28, 77, 99]
temp=list(filter(lambda x:x%2==0,l6))
print (temp)