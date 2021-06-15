class Snake:

    body = []
    head = []
    tail = []
    board=[]

    def __init__(self,body, board):
        self.body = body
        self.head = self.body[0]
        self.tail = self.body[-1]
        self.board=board

    #Return the position of the head
    def getHead(self):
        return self.head
    
    #Return the position of the tail
    def getTail(self):
        return self.tail

    #Try to move the snake to the left without hitting the edge or crossing itself
    def goLeft(self):
        next= [self.head[0]-1,self.head[1]]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next    
            self.move()
            return True

    #Try to move the snake to the right without hitting the edge or crossing itself
    def goRight(self):
        next= [self.head[0]+1,self.head[1]]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next  
            self.move()
            return True
    #Try to move the snake up without hitting the edge or crossing itself
    def goUp(self):
        next= [self.head[0],self.head[1]-1]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next  
            self.move()
            return True

    #Try to move the snake down without hitting the edge or crossing itself
    def goDown(self):
        next= [self.head[0],self.head[1]+1]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next  
            self.move()
            return True

    #Move the snake where the head points
    def move(self):
        self.body.insert(0,self.head)
        self.body.pop(-1)
        self.tail = self.body[-1]

    #check that the head does not collide with the body
    def intersection(self,next):
        if next==self.tail:
            return False
        else:
            return next in self.body
            
    #check that the head does not leave the board
    def crossBoard(self,next):
        if -1 in next:
            return True
        elif next[0]>=self.board[0] or next[1]>=self.board[1] :
            return True
        else:
            return False