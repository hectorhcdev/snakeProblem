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


    #Try to move the path left
    def left(self):
        if self.checkDepth():
            return False
        if self.snake.goLeft():
            self.path.append('L')
            self.stepIncrease()
            return True
        else:
            return False

    #Try to move the path right
    def right(self):
        if self.checkDepth():
            return False
        if  self.snake.goRight() :
            self.path.append('R')
            self.stepIncrease()
            return True
        else:
            return False

    #Try to move the path up
    def up(self):
        if self.checkDepth():
            return False
        if  self.snake.goUp() :
            self.path.append('U')
            self.stepIncrease()
            return True
        else:
            return False

    #Try to move the path down
    def down(self):
        if self.checkDepth():
            return False
        if  self.snake.goDown():
            self.path.append('D')
            self.stepIncrease()
            return True
        else:
            return False

    #Check that the steps are not greater than the depth
    def checkDepth(self):
        #print(self.depth)
        return len(self.path)+1>self.depth

    #Increase the numbers of steps
    def stepIncrease(self):
        self.step=len(self.path)

    #Return the actual step
    def getStep(self):
        return self.step
