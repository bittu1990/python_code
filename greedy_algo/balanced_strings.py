"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings."""

string = 'RLRRLLRLRL'

def balancedStringSplit(string):
    ans = 0
    bal = 0
    for i in string:
        if i == 'R':
            bal += 1
        
        if i == 'L':
            bal -= 1

        if bal == 0:
            ans += 1
    return ans

print (balancedStringSplit(string))
