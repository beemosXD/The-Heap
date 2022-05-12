def gridTraveler(m, n, memo = {}): # adds memo to stop repetition
    key = ("{},{}").format(m,n)
    # are the args in the memo
    if (key in memo): return memo[key]
    if (m ==1) and (n ==1): return 1; # base case 1 by 1 grid has one solution
    if (m==0) or (n == 0): return 0;  # you cant have a grid with a dimension zero  k * 0 is always zero
    
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo);   
    return memo[key]
    

print(gridTraveler(18,18))