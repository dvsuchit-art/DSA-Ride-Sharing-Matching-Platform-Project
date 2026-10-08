import random,time
from .models import Driver,Rider
from .greedy import greedy_match
from .hungarian import hungarian_match
from .cost import build_cost_matrix
def scenario(n,seed=42):
    r=random.Random(seed)
    return ([Driver(f"D{i+1}",r.uniform(0,100),r.uniform(0,100)) for i in range(n)],
            [Rider(f"R{i+1}",r.uniform(0,100),r.uniform(0,100)) for i in range(n)])
def run(label,solver,d,r):
    t=time.perf_counter(); m=solver(d,r); ms=(time.perf_counter()-t)*1000
    return {"algorithm":label,"matches":[x.__dict__ for x in m],"total_distance":sum(x.distance for x in m),"runtime_ms":ms}
def compare_solvers(d,r):
    g=run("Greedy",greedy_match,d,r); o=run("Optimal / Hungarian",hungarian_match,d,r)
    save=g["total_distance"]-o["total_distance"]
    return {"drivers":[x.__dict__ for x in d],"riders":[x.__dict__ for x in r],
            "cost_matrix":build_cost_matrix(d,r),"greedy":g,"optimal":o,
            "distance_saved":save,"distance_saved_pct":save/g["total_distance"]*100 if g["total_distance"] else 0}
def benchmark(sizes=(4,6,8,10,30,100),scenarios_per_size=10,seed=2026):
    out=[]
    for n in sizes:
        gd=od=gm=om=0
        for k in range(scenarios_per_size):
            d,r=scenario(n,seed+n*1000+k); g=run("G",greedy_match,d,r); o=run("O",hungarian_match,d,r)
            gd+=g["total_distance"]; od+=o["total_distance"]; gm+=g["runtime_ms"]; om+=o["runtime_ms"]
        gd/=scenarios_per_size; od/=scenarios_per_size
        out.append({"n":n,"greedy_distance":gd,"optimal_distance":od,"saved_pct":(gd-od)/gd*100,"greedy_ms":gm/scenarios_per_size,"optimal_ms":om/scenarios_per_size})
    return out
