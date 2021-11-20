items = [1,2,3,4,5]

# Big O ==> O(n*n) ==> O(n^2) //Quadratic kind
def logAllPairsOfArray(array):
    for i in array:
        for j in array:
            print(i , j)

# Big O ==> O(n + n^2) ==> O(n^2) //Drop the non-significant one

logAllPairsOfArray(items)

