from snakePath import SnakePath
from snake import Snake
import copy

class FindPaths:

    pathNumbers = 0
    body = []
    board = []
    depth = 0

    def __init__(self, board, body,depth):
        self.board=board
        self.body=body
        self.depth=depth

    def find(self):
        while(False):
            actualPath=self.newPath()
            ##Do Something
            if actualPath.getStep() == 0:
                break
            else:
                self.pathIncrease()

    def newPath(self):
        return SnakePath(self.depth,Snake(self.body,self.board))

    def next(self,path):
        print(path.path)
        
        newPathL=copy.deepcopy(path)
        newPathR=copy.deepcopy(path)
        newPathU=copy.deepcopy(path)
        newPathD=copy.deepcopy(path)

        #print("")
        if newPathL.left():
            #print(newPathL.path)
            result=self.next(newPathL)
            #return result
        print("He pasado por aqui", newPathR.path)
        if newPathR.right():
            result=self.next(newPathR)
            #return result
        if newPathU.up():
            result=self.next(newPathU)
            #return result
            #print(newPathL.path)
        if newPathD.down():
            result=self.next(newPathD)
            #return result
        return None




    def next1(self,path):
        #print(path.left() or path.right() or path.down() or path.up())

        if path.left() or path.right() or path.down() or path.up():
            print(path.path)
            self.next1(path)
        else:
            if path.getStep() != 0:
                self.pathIncrease()
            return path
    
    def pathIncrease(self):
        self.pathNumbers=self.pathNumbers+1
