from snake import Snake
from snakePath import SnakePath

from findPaths import FindPaths
from tests import Test
body1=[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
body2=[[0,2], [0,1], [0,0], [1,0], [1,1], [1,2]]
body3=[[5,5], [5,4], [4,4], [4,5]]

count=0
test1=Test([4, 3],body1,3,7)
if test1.acceptanceTest():
    count=count+1

test2=Test([2, 3],body2,10,1)
if test2.acceptanceTest():
    count = count+1
test3=Test([10, 10],body3,4,81)
if test3.acceptanceTest():
    count=count+1



print("Passed tests : "+str(count)+"/3")
#for i in range(5):
#    print(path.left())
a= Snake(body1,[4,3])
path=SnakePath(3,a)

#path=numbersPaths.newPath()
path.left()
path.left()
path.left()
path.right()
#
print(path.path)
#board= Board([4, 3])