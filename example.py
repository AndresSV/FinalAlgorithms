import readline
from itertools import permutations 

arr1 = []
arr2 = []
values = []


#vertices = input()
#numVertices = int(vertices)

str1 = input()
str2 = input()
str3 = input()

str1_list = str1.split()
map_str1 = map(str, str1_list)

str2_list = str2.split()
map_str2 = map(str, str2_list)

str3_list = str3.split()
map_str3 = map(int, str3_list)

arr1 = list(map_str1)
arr2 = list(map_str2)
values = list(map_str3)

def localMaxValue(setValues):
    result = []
    for i in range(0,8):
        for j in range(0,7):
            if arr1[j+1] == arr2[i]:
                result.append(abs(setValues[i]-setValues[j+1]))
    return result            


print("Values----------------")
print(arr1)
print(arr2)
print(values)

perm = permutations(values)

permutationValues = list(perm)

print("Permutations-------------")
#for i in permutationValues:
#    print(i)

print("Max value Local----------------")


"""
1 2 1 2 3 3 5 4
2 3 3 4 5 6 6 7
2 3 7 5 8 1 6 4


a b a b c c e d
b c c d e f f g
2 3 7 5 8 1 6 4

a a b b c c d e
b c c d d e e d
10 3 1 2 8 2 7 9
"""
listOfResults = []

#for i in permutationValues:
#    listOfResults.append(localMaxValue(i))
optimalValue = max(localMaxValue(permutationValues[0]))
for i in range(0,len(permutationValues)):
    if max(localMaxValue(permutationValues[i])) < optimalValue:
        optimalValue = max(localMaxValue(permutationValues[i]))
        print(optimalValue)
        listOfResults = permutationValues[i]
#maxValue = max(localMaxValue(permutationValues[0]))
#print (i)
print("Results---------------")
print(optimalValue)
print(listOfResults)  

