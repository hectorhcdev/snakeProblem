from snake import Snake
from snakePath import SnakePath


body=[[2,2], [3,2], [3,1], [3,0], [2,0], [1,0], [0,0]]
a= Snake(body,3)
a.goLeft()
a.goLeft()
a.goLeft()
a.goLeft()
a.goLeft()
a.goLeft()
a.goLeft()
a.goLeft()
print(a.goRight())
print(a.body)
#board= Board([4, 3])