import random, time

def fractional_knapsack(products, capacity):
    """Greedy Fractional Knapsack: items can be split."""
    items=sorted(products,key=lambda p: float(p['profit'])/float(p['weight']),reverse=True)
    remaining=float(capacity); total=0.0; selected=[]
    for p in items:
        if remaining<=0: break
        w=float(p['weight']); take=min(w,remaining); fraction=take/w; earned=float(p['profit'])*fraction
        total+=earned; remaining-=take
        if take>0: selected.append({'id':p['id'],'name':p['name'],'weight_taken':round(take,2),'fraction':round(fraction,4),'profit_earned':round(earned,2)})
    return {'algorithm':'Greedy Fractional Knapsack','total_profit':round(total,2),'used_capacity':round(capacity-remaining,2),'remaining_capacity':round(remaining,2),'selected':selected,'time_complexity':'O(n log n)'}

def zero_one_knapsack(products, capacity):
    """Dynamic Programming 0/1 Knapsack: items cannot be split."""
    W=int(capacity); n=len(products); weights=[int(round(float(p['weight']))) for p in products]; profits=[float(p['profit']) for p in products]
    dp=[[0.0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w=weights[i-1]; value=profits[i-1]
        for c in range(W+1):
            dp[i][c]=dp[i-1][c]
            if w<=c: dp[i][c]=max(dp[i][c],value+dp[i-1][c-w])
    selected=[]; c=W
    for i in range(n,0,-1):
        if dp[i][c]>dp[i-1][c]:
            p=products[i-1]; selected.append({'id':p['id'],'name':p['name'],'weight_taken':round(float(p['weight']),2),'fraction':1.0,'profit_earned':round(float(p['profit']),2)}); c-=weights[i-1]
    selected.reverse(); used=sum(x['weight_taken'] for x in selected)
    return {'algorithm':'Dynamic Programming 0/1 Knapsack','total_profit':round(dp[n][W],2),'used_capacity':round(used,2),'remaining_capacity':round(max(0,capacity-used),2),'selected':selected,'time_complexity':'O(n × W)','capacity_note':'DP rounds product weights to nearest whole unit and rounds capacity down to an integer.'}

def benchmark_algorithms():
    results=[]
    for n in (10,25,50,100):
        sample=[{'id':i,'name':f'Item {i}','weight':random.randint(1,15),'profit':random.randint(10,100)} for i in range(n)]
        cap=100; start=time.perf_counter(); fractional_knapsack(sample,cap); greedy=(time.perf_counter()-start)*1000
        start=time.perf_counter(); zero_one_knapsack(sample,cap); dp=(time.perf_counter()-start)*1000
        results.append({'products':n,'capacity':cap,'greedy_ms':round(greedy,4),'dp_ms':round(dp,4)})
    return results
