def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('Do you really want to quit?')
L=[]
a=3
L.append(a)
print(a , L)
print ("*"*20)
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
def f(a, L=[]):
    L.append(a)
    print(a)
    return L

# print(f(1))
# print (L)

print(f(2))
print(f(3))

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.", 1,
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

import io
b = io.BytesIO(b"abcdef")
view = b.getbuffer()
view[2:4] = b"56"
print (b.getvalue())
# b'ab56ef'


from collections import deque
queue = deque(["Eric", "John", "Michael"])
print (queue)
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
print (queue)
queue.popleft() 
print (queue)                # The second to arrive now leaves
# 'John'
# Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
print (queue)  

capitals = {"svk":"Bratislava","deu":"Berlin", "dnk":"Copenhagen"}

print( len(capitals))

x = []
for i in range(4):
    x.append(list(range(4)))

print (x)

y = list(range(10))
print(y)

z = [None]*10

print (z)

print(z.pop(), len(z))

