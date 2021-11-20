# Given two arrays, create a function that 
# lets a user (true / false) whether these 2 arrays
# contain any common items
# For example:
# const array1: ['a', 'b', 'c', 'x']
# const array2: ['z', 'y', 'i']
# output should be False
# //
# const array1: ['a', 'b', 'c', 'x']
# const array2: ['z', 'y', 'x']
# should return true

# are there only two arrays
# is it fixed size or the size of the array can be of any size
# can the array have primitive values (integer, float etc)
# is time / space complexity is of importance here. i.e. should code be efficient

#1. Start with naive brute force approach (you dont need to write any code, just speak about it)

# Big O ==> O (n^2) # not the best solution and can be improved
# not readable (complicated and hard to read for other developers)

def matchingElementsFound(array1, array2):
    returnVal = False
    for i in range (len(array1)):
        for j in range (len(array2)):
            if array1[i] == array2[j] :
                returnVal = True
                break
    return returnVal
        

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']
print(matchingElementsFound(array1, array2))

array3 = ['a', 'b', 'c', 'x']
array4 = ['z', 'y', 'i']
print(matchingElementsFound(array3, array4))

# Is there a better way to handle and avoid time complexity of O(n^2)
# Think of hash tables / converting first array into object and using second array to check if the property exists 
# e.g. 
# array1 = {
#    a: true,
#    b: true,
#    c: true,
#    x: true
# }
# array2[index] == array.property

# O(a+b)
def containsCommonItem(array1, array2):
    class arr1:
        pass

    for i in array1:
        # 1 - create object where properties == items in the array
        # 2 - loop through second array and check if item in second array matches with the object property we created earlier
        # 1
        arr1.add



