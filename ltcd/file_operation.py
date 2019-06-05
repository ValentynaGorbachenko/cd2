
'''
with open('text.txt', 'w') as f:
    read_data = f.write("hey1\nhey2\nhey3")
    print(read_data)
    print(type(read_data))
    


print(f.closed)
'''
f = open('text.txt', 'r+') # reading and writing 'a' - appned 

# print(f.read(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')
# print(f.readline(),end='')

# fl = list(f)
# for i in range(len(fl)):
#     print(fl[i], end='')

import json

x=json.dumps([1, 'simple', 'list'])
print(x, type(x))


# write into the file
json.dump(x, f)
f.seek(0)
print(f.readline())
f.seek(0)
# y = json.loads(f)

y = json.loads(f.read())

print(y, type(y))
# y = json.loads(y)

print(y, type (y))
for el in y:
    print(el)

f.close()