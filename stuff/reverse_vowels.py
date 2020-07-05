"""Given a string, swap the position of the vowels
i/p: "apples and oranges"
o/p: "epplas ond arengas" """

input = 'fhdfjfehjewkfb hefehwoueefbkbv  fhuheufebfbfe wiuewehewfew  uerieirhewnewiofg;bdrbfrbbbdisi'
def isVowel(char):
    vowel = 'aeiou'
    if char in vowel:
        return True
    else:
        return False

def reverseVowels(input):
    ipLength = len(input)
    start = 0
    end = ipLength - 1
    swapMap = {}

    while start <= end :
        if not isVowel(input[start]):
            start += 1
            continue

        if not isVowel(input[end]):
            end -= 1
            continue

        swapMap[start] = input[end]
        swapMap[end] = input[start]

        start += 1
        end -=1

    swappedString =''
    for i in range(ipLength):
        if isVowel(input[i]):
            swappedString += swapMap[i]
        else:
            swappedString += input[i]
    
    return swappedString

print(input)
print(reverseVowels(input))