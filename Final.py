import readline
from itertools import permutations
from numpy import random
import numpy as np
import sys 


def swapTwoValues(u,v,perm):
    tmp = perm[u]
    perm[u] = perm[v]
    perm[v] = tmp
    return perm

def swapThreeValues(u,v,w,perm):
    tmp = perm[u]
    perm[u] = perm[v]
    perm[v] = perm[w]
    perm[w] = tmp
    return perm

def shiftLeft(perm, n):
    if n > 0:
        perm.insert(0, perm.pop(-1))
        shiftLeft(perm, n-1)
    return perm

def localMaxValue(verticesOne,verticesTwo, values):
    result = []
    for i in range(0,len(verticesOne)):
        for j in range(0,len(verticesTwo)-1):
            if verticesOne[j+1] == verticesTwo[i]:
                result.append(abs(values[i]-values[j+1]))
    maxLocalValue = max(result)
    return maxLocalValue           

def entryArgs():
    content = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        content.append(line)

    content.pop(0)
    header = content[0].split()
    content.pop(0)

    nodesOneLen = int(header[0])
    nodesTwoLen = int(header[1])
    edgesLen = int(header[2])
    contentLen = len(content)

    nodesOneList = []
    nodesTwoList = []

    for i in range(0,contentLen):
        tmp = content[i].split()
        nodesOneList.append(int(tmp[0]))

    for i in range(0,contentLen):
        tmp = content[i].split()
        nodesTwoList.append(int(tmp[1]))

    valuesList = []
    for i in range(1,edgesLen+1):
        valuesList.append(i)

    randomPer = list(random.permutation(valuesList))
    listOfVals = []
    listOfVals.append(nodesOneList)
    listOfVals.append(nodesTwoList)
    listOfVals.append(randomPer)
    return listOfVals

def pickAtRandom(x, perm):
    res = []
    if x==1:
        u = random.randint(1,len(perm))
        v = random.randint(1,len(perm))
        res = swapTwoValues(u,v,perm)

    elif x==2:
        u = random.randint(1,len(perm))
        v = random.randint(1,len(perm))
        w = random.randint(1,len(perm))
        res = swapThreeValues(u,v,w,perm)

    elif x==3:
        res = shiftLeft(perm, 1)
    
    return res

def localSearch(x, vOne, vTwo, perm):
    bestCost = localMaxValue(vOne,vTwo,perm)
    if x==1:
        mejora=True
        while mejora:
            mejora = False
            for i in range(0,len(perm)):
                for j in range(0,len(perm)-1):
                    pPrime = swapTwoValues(i,j,perm)
                    pPrimeCost = localMaxValue(vOne,vTwo,pPrime)
                    #print(pPrimeCost)
                    if pPrimeCost < bestCost:
                        bestCost = pPrimeCost
                        mejora = True
                    perm = swapTwoValues(i,j,perm)

    elif x==2:
        mejora=True
        while mejora:
            mejora = False
            for i in range(0,len(perm)):
                for j in range(0,len(perm)-1):
                    for k in range(0, len(perm)-2):
                        pPrime = swapThreeValues(i,j,k,perm)
                        pPrimeCost = localMaxValue(vOne,vTwo,pPrime)
                        #print(pPrimeCost)
                        if pPrimeCost < bestCost:
                            bestCost = pPrimeCost
                            mejora = True
                        perm = swapThreeValues(i,j,k,perm)

    elif x==3:
        mejora=True
        while mejora:
            mejora = False
            for i in range(0,len(perm)):
                pPrime = shiftLeft(perm,i)
                pPrimeCost = localMaxValue(vOne,vTwo,pPrime)
                #print(pPrimeCost)
                if pPrimeCost < bestCost:
                    bestCost = pPrimeCost
                    mejora = True
                perm = shiftLeft(perm,i)
    
    return bestCost
#-----------------Here starts the main method-----------
vals = entryArgs()

nodesOne = vals[0]
nodesTwo = vals[1]
randomPer = vals[2]

s = localMaxValue(nodesOne,nodesTwo,randomPer)

#print(randomPer)
flag = 1
while flag < 2:
    k = 1
    while k < 4:
        #Pick one neighborhood random
        sOne = pickAtRandom(k,randomPer)
        #print(sOne)
        sOneCost = localSearch(k,nodesOne,nodesTwo,sOne)

        if sOneCost < s:
            s= sOneCost
        else:
            k+=1
    flag+=1
        
print(s)
