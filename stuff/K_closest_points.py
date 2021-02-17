"""1) Given a list of points as [x,y] pairs; a vertex in [x,y] form; and an integer k,
 return the kth closest points in terms of Euclidean distance

2) Assuming that the dataset is too big to store in memory, 
rewrite functions for distributed system"""

points = [[1,2], [2,3], [1,-1]]
vertex = [2,2]
k=2

import math 
def get_distnace(p1, p2):
    dist_sqr = []
    for a,b in zip(p1,p2):
        dist_sqr.append((a + b) ** 2)
    sqr_sum = sum(dist_sqr)
    return math.sqrt(sqr_sum)

def k_dist(vertex, points, k):
    distance = []
    for i, pt in enumerate(points):
        distance.append([get_distnace(vertex, pt), i])
    print(distance)
    result = []
    for i in sorted(distance)[:k]:
        result.append(points[i[1]])
    
    return result

print(k_dist(vertex, points, k))