"""Sort charecters by frequency, if same frequency then by order
tree => eert
banana => aaannb
"""
from collections import Counter

def sort_by_freq(input):
    freq_dict = {}
    ans =''
    for i in input:
        if i in freq_dict.keys():
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    
    for j in sorted(freq_dict, key = freq_dict.get, reverse = True):
        ans += j*freq_dict[j]

    return ans

def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    counter = Counter(s)
    output = "".join(char * freq for char, freq in counter.most_common())
    return output

input ="kokilabenedueqoensoienwdiefojkwdnksd"
print(frequencySort(input))
