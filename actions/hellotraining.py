import sys
from st2common.runners.base_action import Action

class MyAction(Action):
    n1 = 0
    n2 = 1
    count = 0
    def run(self, a):
        if a<=1 :
            print("Enter a number greater than 1")
        else :
            print("Fibonacci sequence upto",a,":")
            while self.count < a:
                print(n1)
                nth = n1 + n2
                # update values
                self.n1 = n2
                self.n2 = nth
                self.count += 1
        return(True)
