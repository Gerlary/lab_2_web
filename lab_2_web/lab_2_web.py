from math import ceil

cache = {}

"""
{   
    "func_name": {
        "count": 5,
        "value": "res"
    }
}
"""

def decorator(count):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}::{args}::{kwargs}"
            cached_value = cache.get(key)
            if cached_value is None:
                res = func(*args, **kwargs)
                cache[key] = {"count": count, "value": res}
                return res
            else:
                counter = cached_value["count"]
                value = cached_value["value"]
                counter -= 1
                cache[key] = {"count": counter, "value": value}
                if counter <=0:
                    cache.pop(key)
                return value
        return wrapper
    return outer_wrapper

@decorator(count = 2)
def func1():
    a = int(input("Является ли число полиндромом? :"))
    a = list(str(a))
    f = a[ceil(len(a)/2):]
    f.reverse()
    a = a[:len(a)//2]   
    if f == x:
        print("True")
        return 
    print("False")
    

@decorator(count = 2)
def func2():
    inp = list(map(int,input("Введите список чисел: ").split()))
    even = []
    tric = []
    fifc = []
    for i in inp:
        if i%3 == 0:
            tric +=[i]
        if i%2 == 0:
            even += [i]
        if i%5 == 0:
            fifc += [i]
    print("четные{}\nкратные 3-м{}\nкратные 5-ти{}".format(even,tric,fifc))
    
@decorator(count = 2)
def func3():
    x = int(input("Введите число: "))
    flag = False
    if x <0:
        flag = True
    x = str(x)
    if flag:
        x = x[1:]
    x = x[::-1]
    x = int(x)
    if flag:
        x *=-1
    return x

@decorator(count = 2)
def func4():
    A = float(input("Введите число: "))
    n = int(input("Введите степень корня: "))
    x0 = A/2
    for i in range(1000) :
        x0 = 1/n*((n-1)*x0+A/x0**(n-1))
    print (x0)
@decorator(count = 2)
def func5(x):
    inp = int(input("Введите число: "))
    for i in range(2,x//2):
        if x%i ==0:
            print("Не простое число")
            return 
    print("Простое число")



f = int(input("Введите номер выводимой функции"))
if f == 0:
    
    func1()
elif f == 1:
    
    func2()
    
elif f == 2:
    
    func3()
elif f == 3:
    func4()
elif f == 4:
    
    func5()
else:
    print("ERROR")


