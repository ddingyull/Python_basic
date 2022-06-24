def sum_func(n):
    s = 0
    for x in range(1, n+1):
        s = s+x
    return s

print(sum_func(10))
print(sum_func(100))

#1부터 n을 곱을 구하는 함수
def factorial(n):
    s = 1
    for x in range(1, n+1):
        s = s * x
    return s

print(factorial(5))
print(factorial(10))

import turtle as t
t.shape('turtle')
def angle(n):
    for x in range(n):
        t.fd(50)
        t.lt(360/n)

def angle2(n,a):
    for x in range(n):
        t.fd(a)
        t.lt(360/n)

angle(3)
angle(5)


t.up()
t.d(100)
t.down()

abgle2(3, 75)
abgle2(5, 100)



