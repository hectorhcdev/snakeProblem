class Snake:

    body = []
    head = []
    tail = []
    step = 0
    depth = 0

    def __init__(self,body,depth):
        self.body = body
        self.depth = depth
        self.head = self.body[0]
        self.tail = self.body[-1]
        print(self.body)

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def goLeft(self):
        next= [self.head[0]-1,self.head[1]]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next    
            self.move()
            return True

    def goRight(self):
        next= [self.head[0]+1,self.head[1]]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next  
            self.move()
            return True

    def goUp(self):
        next= [self.head[0],self.head[1]-1]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next  
            self.move()
            return True

    def goDown(self):
        next= [self.head[0],self.head[1]+1]
        if self.intersection(next) or self.crossBoard(next):
            return False
        else:
            self.head=next  
            self.move()
            return True

    def move(self):
        self.body.insert(0,self.head)
        self.body.pop(-1)
        self.tail = self.body[-1]

    def intersection(self,next):
        if next==self.tail:
            return False
        else:
            return next in self.body

    def crossBoard(self,next):
        return -1 in next       