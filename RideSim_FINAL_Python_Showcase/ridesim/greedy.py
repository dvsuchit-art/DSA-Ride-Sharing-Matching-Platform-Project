from .cost import build_cost_matrix
from .models import Match
def greedy_match(drivers,riders):
    if len(drivers)!=len(riders): raise ValueError("Equal driver/rider counts required")
    c=build_cost_matrix(drivers,riders); remaining=set(range(len(riders))); out=[]
    for i in range(len(drivers)):
        j=min(remaining,key=lambda x:(c[i][x],x)); remaining.remove(j)
        out.append(Match(i,j,c[i][j]))
    return out
