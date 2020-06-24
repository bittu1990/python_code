"""Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000."""

def pallindromic(vchar: str):
        if vchar == vchar[::-1]:
            return True

def longPalSub(char: str):
        result = ""
        v_max=0
        for i, w in enumerate(char):
            for n, v in  enumerate(char[i:]):
                if w == v and pallindromic(char[i:i+n+1]) and v_max<(n+1) :
                    v_max=n+1
                    result = char[i:i+n+1]
                    #print(result) 
        return result
      
subString = 'babaaabd'

print(longPalSub(subString))