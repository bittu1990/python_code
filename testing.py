A = [-1, -3]
ans = []
for i in range(len(A)-1):
    if sorted(A, reverse = True)[i] > sorted(A, reverse = True)[i+1]:
        if (sorted(A, reverse = True)[i-1] +1) not in A:
            if (sorted(A, reverse = True)[i-1] +1) < 0:
                ans.append(0)
            else:
                ans.append(sorted(A, reverse = True)[i-1] +1)
print(ans)
print(min(ans))

        
            
            
    
