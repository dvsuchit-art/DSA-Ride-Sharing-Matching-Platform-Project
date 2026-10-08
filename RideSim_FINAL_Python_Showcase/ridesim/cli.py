from .engine import scenario,compare_solvers,benchmark
def main():
    d,r=scenario(6,7); x=compare_solvers(d,r)
    print("RIDESIM — DRIVER-RIDER MATCHING ENGINE")
    for k in ("greedy","optimal"):
        a=x[k]; print("\n"+a["algorithm"])
        for m in a["matches"]: print(f"D{m['driver_index']+1} -> R{m['rider_index']+1}: {m['distance']:.3f} km")
        print(f"Total: {a['total_distance']:.3f} km | {a['runtime_ms']:.3f} ms")
    print(f"Saved: {x['distance_saved']:.3f} km ({x['distance_saved_pct']:.1f}%)")
    print("\nBenchmark")
    for a in benchmark(): print(a)
if __name__=="__main__": main()
