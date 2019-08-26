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
            print("Fibonacci sequence upto",nterms,":")
            while count < nterms:
                print(n1,end=' , ')
                nth = n1 + n2
                # update values
                n1 = n2
                n2 = nth
                count += 1
        return(True)
