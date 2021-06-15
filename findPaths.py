from snakePath import SnakePath
from snake import Snake
import random
import copy

class FindPaths:


    pathSecuence=[]
    pathNumbers = 0
    body = []
    board = []
    depth = 0

    def __init__(self, board, body,depth):
        self.board=board
        self.body=body
        self.depth=depth
        self.pathSecuence=[]
        self.pathNumbers = 0

    #Iterates and returns all found routes
    def find(self,rep):
        actualPath=self.newPath()
        for _ in range(rep):
            actualPath=self.next(actualPath)
        print("Valid paths: ",self.pathSecuence)
        return self.pathNumbers

    #Return a new path
    def newPath(self):
        return SnakePath(self.depth,copy.copy(Snake(copy.copy(self.body),self.board)))

    #Increase the number of paths found
    def pathIncrease(self):
        self.pathNumbers=self.pathNumbers+1


    #Generates a new random position and tries to reach it, if it has already been found, it is discarded
    def next(self, path):
        if path.checkDepth() and len(path.path)>0:

            if  not path.path in self.pathSecuence:
                self.pathIncrease()
                self.pathSecuence.append(path.path)

            return self.newPath()

        nextPath=random.randint(0,3)

        if nextPath==0:
            path.left()
        if nextPath==1:
            path.right()
        if nextPath==2:
            path.up()
        if nextPath==3:
            path.down()
        return path
        
        
