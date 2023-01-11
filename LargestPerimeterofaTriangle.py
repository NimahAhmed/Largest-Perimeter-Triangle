
'''This function returns the larges perimeter of a triangle with a non-zero area
from 3 lengths in a given list'''

#Step 1: find out if triangle is possible from 3 given lengths

def isTrianglePossible(lst):
    i=0
    if lst[i]+lst[i+1]>=lst[i+2] and lst[i+1]+lst[i+2]>=lst[i] and lst[i]+lst[i+2]>=lst[i+1]:
        print('Triangle Possible')
    else:
        print('Triangle not Possible')

mylist1=[1,2,3]
mylist2=[1,2,4]
mylist3=[3,4,5]

# isTrianglePossible(mylist1)
# isTrianglePossible(mylist2)
# isTrianglePossible(mylist3)

#Step 2: If, triangle is possible, then add three values to get Perimeter.
#Return 0 if triangle is not possible.

def getPerimeter(lst):
    # i=0
    if lst[0]+lst[1]>lst[2] and lst[1]+lst[2]>lst[0] and lst[0]+lst[2]>lst[1]:
        return (lst[0]+lst[1]+lst[2])
    else:
        return 0

mylist1=[1,2,3]
mylist2=[2,3,4]
mylist3=[3,4,5]
mylist4 = [4,10,11]

# print(getPerimeter(mylist4))
# getPerimeter(mylist2)
# getPerimeter(mylist3)

#Step 4- now def a func that will take greater than 3 values as argument
#and return the largest possible perimeter

def getLargestPerimeter(lst):
    currLargestPerim = 0
    i=0
    while i<len(lst)-2:
        print(i)
        currPerim = getPerimeter([lst[i], lst[i+1], lst[i+2]])
        print("current: ", currPerim)
        if currPerim > currLargestPerim:
            currLargestPerim = currPerim
            print("found larger: ", currLargestPerim)
        i+=1
    if currLargestPerim==0:
        print('No triangles possible')
    return currLargestPerim

mylist1=[1,2,3,0]
mylist2=[2,3,4,10,11]
mylist3=[1,2,2,3]

largest_perim = getLargestPerimeter(mylist1)
print(largest_perim)
