from findPaths import FindPaths
class Test:

    board=[]
    body=[]
    depth=0
    result=0
    def __init__(self,board,body,depth,result):
        self.board=board
        self.body=body
        self.depth=depth
        self.result=result

    def acceptanceTest(self,reps):
        a=FindPaths(self.board,self.body,self.depth)
        if self.result != a.find(reps):
            print("Fail in Test", "Result: "+str(self.result)+" your result: "+str(a.pathNumbers))
            return False
        else:
            print("Pass", "Result: "+str(self.result)+" your result: "+str(a.pathNumbers))
            return True