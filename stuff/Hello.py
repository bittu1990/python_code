l1 = ["egg","butter","milk"]
s1 = [4,8,2]
l2 = ["egg","milk"]
s2 = [4,3]

d1 = dict (zip(l1,s1))
d2 = dict (zip(l2,s2))

print(d1)
print(d2)
count = 0
for key in d1.keys():
    if key in d2.keys():
        if d1[key] != d2[key]:
            count += 1

print(count)