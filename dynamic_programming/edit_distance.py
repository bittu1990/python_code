"""Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character"""

import numpy as np
source = 'intention'
target = 'execution'

def minEditDist(target, source):

    target = '$'+target
    source = '$'+source
    
    sol = np.zeros((len(source), len(target)))

    sol[0] = [i for i in range(len(target))]
    sol[:,0] = [j for j in range(len(source))]

    for c in range(1, len(target)):
        for d in range(1, len(source)):
            if target[c] != source[d]:
                sol[d,c] = min(sol[d-1,c], sol[d,c-1]) +1
            else:
                sol[d,c] = sol[d-1, c-1]
    
    return sol



############################################################################

def minDIstance(source, target):
    dp = [[0]*(len(target)+1) for j in range(len(source)+1)]

    for i in range(1, len(source)+1):
        dp[i][0] = dp[i-1][0]+1
    
    for i in range(1, len(target)+1):
        dp[0][i] = dp[0][i-1]+1

    for i in range(1, len(source)+1):
        for j in range(1, len(target)+1):
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (0 if source[i-1] == target[j-1] else 1))
    return dp[-1][-1]

print(minDIstance(source, target))
