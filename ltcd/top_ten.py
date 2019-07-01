#!/usr/local/bin/python3

# make file executabel 
# add this to the top of the file #!/usr/local/bin/python3
# in terminal for the carrent session add path $ PATH=$PATH:/Users/Valentynka/vg/ltcd
# change the mode $ chmod 755 ( to chnage it back $ chmod 644)
# run file in terminal 
# $ top_ten.py

def top_ten(arr):
    if (len(arr)<=10):
        arr.sort()
        return arr
    arr.sort()
    return arr[len(arr)-10:len(arr)]

print(top_ten([3,1,3,5]))
print(top_ten([2,1,4,2,-1,3,5,9,12,12,34,23]))
