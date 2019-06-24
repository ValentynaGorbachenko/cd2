'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''

def reorderLogFiles(logs): # doesn't work for all cases
    def my_sort(a):
        return a[1]

    print(logs)
    if len(logs) < 1:
        return logs
    temp_logs, res_letters, res_digits, res = [], [], [], []

    # split each log and make it an array
    for el in logs:
        temp_logs.append(el.split(" "))

    print(temp_logs)

    
    for log in temp_logs:
        if log[1].isdigit():
            res_digits.append(log)
        elif log[1].isalnum():
            res_letters.append(log)
    
    res_letters.sort(key=my_sort)
    res_letters.extend(res_digits)

    print(res_letters)

    for i, item in enumerate(res_letters):
        res_letters[i] = " ".join(item)

    print(res_letters)
    return res_letters

def reorderLogFiles2(logs): # very short solution :)
    def f(log):
        id_, rest = log.split(" ", 1)
        # print(id_, " and ", rest)
        return (0, rest, id_) if rest[0].isalpha() else (1,)

    return sorted(logs, key = f)
    

# print(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
print(reorderLogFiles2(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))
# ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


def reorderLogFiles4(logs): # modified mine solution 
    def my_sort(a):
        return(a[1], a[0])

    print(logs)
    if len(logs) < 2:
        return logs

    temp_logs, res_letters, res_digits = [], [], []

    # split each log and make it an array
    for el in logs:
        temp_logs.append(el.split(" ",1))

    print(temp_logs)

    
    for log in temp_logs:
        if log[1][0].isdigit():
            res_digits.append(log)
        else:
            res_letters.append(log)
    print("res_letters is ", res_letters)

    res_letters.sort(key=my_sort)
    res_letters.extend(res_digits)

    print(res_letters)

    for i, item in enumerate(res_letters):
        res_letters[i] = " ".join(item)

    print(res_letters)
    return res_letters


# print(reorderLogFiles4(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))


