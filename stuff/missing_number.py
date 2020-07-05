num = [5,7,2,3,6]

def findSmallestMissingNumber(num):
    maxNumber = max(num)
    #Sum of n consecutive numbers is (n(n+1))/2
    totalSum = int((maxNumber * (maxNumber + 1)) / 2 )
    missingNumber = totalSum - sum(num)
    if missingNumber in num:
        for i in range(len(num)):
            if num[i] > missingNumber:
                print(i)
                num.pop(i)
    return num

print(findSmallestMissingNumber(num))