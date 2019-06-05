import json

# open('text1.txt','x') #can be done only once - raises error if file exists
arr = ['string', [1,2,3], True, 'another string']
with open('text1.txt', 'r+') as f:
    f.write(str(json.dumps(arr*2))) # fully rewrrite a file
    json.dump(json.dumps(arr), f) # appends values
    print(f.tell())
    f.seek(0)
    print(f.tell())
    f_data = f.read()
    print(f_data)
    
    # data = json.loads(f.read())
    
    for line in f_data: 
        print (line)
    # for x in f:
    #     print(x, end='')
    f.close()