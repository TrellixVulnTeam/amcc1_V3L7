'''

a = 210
b = "this is a string"

print(a,b)


'''

x = 21 #010101
y = 3  #

print(x | y)
print(x & y)


# iseng-iseng doang, jgn dilihat, jelek :)

'''
def recursion(x):
    if(x <= 1):
        return 1
    else:
        return (recursion(x-1) + recursion(x-2))

def euler(x):
    e = 0
    for n in range(x):
        e += 1/factorial(n)
    return e

def factorial(x):
    if(x <= 0 or x == 1):
        return 1
    else:
        return x*factorial(x-1)

def collatz(x):
    global count
    #print(x)
    count += 1
    if(x == 1):
        print("total step :", count)
        return 1
    elif(x%2 == 0):
        return collatz(x/2)
    else:
        return collatz(3*x+1)

count = -1
collatz(10)

'''

