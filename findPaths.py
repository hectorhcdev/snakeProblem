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

    def find(self,rep):
        actualPath=self.newPath()
        for _ in range(rep):
            actualPath=self.next(actualPath)
            ##Do Something
            #if actualPath.getStep() == 0:
            #    break
            #else:
            #    self.pathIncrease()
        print(self.pathSecuence)
        return self.pathNumbers

    def newPath(self):
        return SnakePath(self.depth,copy.copy(Snake(copy.copy(self.body),self.board)))

    def pathIncrease(self):
        self.pathNumbers=self.pathNumbers+1

    def next(self, path):
        #prevLen=len(path.path)
        if path.checkDepth() and len(path.path)>0:
            if  not path.path in self.pathSecuence:
                self.pathIncrease()
                self.pathSecuence.append(path.path)
            return self.newPath()
        nextPath=random.randint(0,3)
        #print(nextPath)
        #print(path.path)
        if nextPath==0:
            path.left()
        if nextPath==1:
            path.right()
        if nextPath==2:
            path.up()
        if nextPath==3:
            path.down()
        return path
        
        
