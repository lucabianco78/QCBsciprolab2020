L1 = [1,1, 13, 22, 7, 43, 81, 77, 12, 15,21, 84,100]
L2 = [44,32,7, 100, 81, 13, 1, 21, 71, 7]

L1.sort()
L2.sort()
intersection = [x for x in L1 if x in L2]

print("L1:    ", L1)
print("L2:    ", L2)
print("inters:", intersection)


intersection2 = [L1[x] for x in range(len(L1)) if L1[x] in L2 and L1[x] not in  L1[x+1:]]
print(intersection2)