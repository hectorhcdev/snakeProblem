from snake import Snake
class SnakePath:

    step=0
    depth=0
    path=[]
    snake=None

    def __init__(self,depth,snake):
        self.depth=depth
        self.snake=snake
        self.step=0
        self.path=[]

    def left(self):
        if self.checkDepth():
            return False
        if self.snake.goLeft():
            self.path.append('L')
            self.stepIncrease()
            return True
        else:
            return False

    def right(self):
        if self.checkDepth():
            return False
        if  self.snake.goRight() :
            self.path.append('R')
            self.stepIncrease()
            return True
        else:
            return False

    def up(self):
        if self.checkDepth():
            return False
        if  self.snake.goUp() :
            self.path.append('U')
            self.stepIncrease()
            return True
        else:
            return False

    def down(self):
        if self.checkDepth():
            return False
        if  self.snake.goDown():
            self.path.append('D')
            self.stepIncrease()
            return True
        else:
            return False
    def checkDepth(self):
        #print(self.depth)
        return len(self.path)+1>self.depth

    def stepIncrease(self):
        self.step=len(self.path)

    def getStep(self):
        return self.step
