#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    for x in a:
        res += x
    return res
    #adding a comment to check workflow
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
