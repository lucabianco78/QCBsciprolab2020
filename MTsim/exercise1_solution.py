def find_missing(S):
    if len(S) > 0:
        m = max(S)
        vals = [ 0 for i in range(m)]
        for x in S:
            if x < 0:
                print("Warning {} is <0. Ignoring it.".format(x))
            else:
                vals[x-1] += 1
        return [x+1 for x in range(m) if vals[x] == 0]
    else:
        print("Warning: list is empty. Returning None")
        

if __name__ == "__main__":
    
    S = [1,9,7, 7, 4, 3, 3, 3]
    S1 = list(range(10))
    print(find_missing(S))
    print(find_missing(S1))
    print(find_missing([]))
    S2 = [1, -72, 4, -3, -3, 3,10]
    M = find_missing(S2)
    print(M) 
