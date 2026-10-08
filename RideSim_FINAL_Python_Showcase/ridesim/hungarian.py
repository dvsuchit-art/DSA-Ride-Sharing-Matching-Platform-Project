from .cost import build_cost_matrix
from .models import Match
def _hungarian(a):
    n=len(a)
    if any(len(x)!=n for x in a): raise ValueError("Square matrix required")
    u=[0.0]*(n+1); v=[0.0]*(n+1); p=[0]*(n+1); way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i; j0=0; mn=[float("inf")]*(n+1); used=[False]*(n+1)
        while True:
            used[j0]=True; i0=p[j0]; delta=float("inf"); j1=0
            for j in range(1,n+1):
                if not used[j]:
                    cur=a[i0-1][j-1]-u[i0]-v[j]
                    if cur<mn[j]: mn[j]=cur; way[j]=j0
                    if mn[j]<delta: delta=mn[j]; j1=j
            for j in range(n+1):
                if used[j]: u[p[j]]+=delta; v[j]-=delta
                else: mn[j]-=delta
            j0=j1
            if p[j0]==0: break
        while True:
            j1=way[j0]; p[j0]=p[j1]; j0=j1
            if j0==0: break
    ans=[-1]*n
    for j in range(1,n+1):
        if p[j]: ans[p[j]-1]=j-1
    return ans
def hungarian_match(drivers,riders):
    if len(drivers)!=len(riders): raise ValueError("Equal driver/rider counts required")
    c=build_cost_matrix(drivers,riders); a=_hungarian(c)
    return [Match(i,j,c[i][j]) for i,j in enumerate(a)]
