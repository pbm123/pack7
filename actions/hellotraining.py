import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c):
        print("Sum="+str(a+b+c))
        print("Type of a= "+str(type(a)))
        print("Type of b= "+str(type(b)))
        print("Type of c= "+str(type(c)))
        return(True,a+b+c)
