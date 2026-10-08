import math
def euclidean(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])
def build_cost_matrix(drivers,riders):
    return [[euclidean((d.x,d.y),(r.x,r.y)) for r in riders] for d in drivers]
