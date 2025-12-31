# functions


def func():
    a = 3
    def func2():
        a = 5
        print(a)
    func2()
    print(a)

print(func())



def add(a, b):
    return a + b

result = add(2, 3)
print(result)


def call_with_names(first, second, third):
    print(f"first: {first}")
    print(f"second: {second}")
    print(f"third: {third}")
    
call_with_names(second=2, first=1,third=3)




def variable_length_args(*args):
    
    print(f"type of args: {type(args)}")
    
    for arg in args:
        print(arg)
        
variable_length_args('a', 1, (2, 3,), [2, 'b'],2.14)



def variable_length_kwargs(**kwargs):
    
    print(f"type of kwargs: {type(kwargs)}")
    
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
variable_length_kwargs(first='a', second=1, third=(2, 3,), fourth=[2, 'b'], fifth=2.14)


data = [(3, 'b'), (2, 'a'), (1, 'c')]
print(sorted(data, key=lambda data: data[0]))



pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(f"sorted pairs: {pairs}")

def greet(name, verbose=False):
     if verbose:
         print(f"Hello, {name}! Welcome to Real Python!")
     else:
         print(f"Hello, {name}!")


greet("Pythonista",verbose=True)
#Hello, Pythonista! Welcome to Real Python!

greet("Pythonista")
# Hello, Pythonista!


def append_to(item, target=[]):
    target.append(item)
    return target

print(append_to(1))
print(append_to(2))



def function(x, y, /, z, w, *, a, b):
     print(x, y, z, w, a, b)
function(1,2,3,w=4,a=1,b=7)


x = 10

def test():
    global x
    x = 20

test()
print(x)


def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)

outer()


def add_us(a, b):
    c = a + b
    return c

a = float(input())
b = float(input())

ans=add_us(a, b)

print(ans)

def demo():
    print("hello")
print(demo())

def demo():
    return 'hello'
print(demo())


def function(x, y,z,a):
      print(x, y, z,a)
function(5,3,3,a=3)


def demo(a, *args, b=10, **kwargs):
    print("a =", a)
    print("args =", args)
    print("b =", b)
    print("kwargs =", kwargs)
demo(1,3,4,5,b=6,c=7,d=8)
print(print(print((print()))))



dict={'1':'krish' , '2':'tanish','3':'paraj'}
for key, value in dict.items():
    print(f"{key} = {value}")
else:
    print("complete dict printed")
    
    
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(f"sorted pairs: {pairs}")

pairs = {1:'one', 2:'two', 3:'three', 4:'four'}
pairs=sorted(pairs.items(),key=lambda pair: pair[1])
print(f"sorted pairs: {pairs}")

get_value = lambda d, k: d.get(k)
print(get_value({1: 1, 2: 2}, 2))  