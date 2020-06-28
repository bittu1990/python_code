"""Given a string, find the length of the longest substring without repeating characters."""
substr = 'wab'

def lengthOfLongestSubstring(subsstr):
    if len(substr) == 0:
        return 0
    if len(substr) == 1:
        return 1
    
    max_val = 0
    for i in range(len(substr)):
        j = i
        d = {}

        for j in range(i, len(substr)):
            if substr[j] not in d.keys():
                d[substr[j]] = 1
            elif substr[j] in d.keys():
                break
        print(d)
        curr_val = len(d.keys())
        if curr_val > max_val:
            max_val = curr_val

    return max_val
    

print(lengthOfLongestSubstring(substr))