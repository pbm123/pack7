import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, a,b,c):
        print("Sum="+str(a+b+c))
        print("Type of a= "+type(a))
        print("Type of b= "+type(b))
        print("Type of c= "+type(c))
        return(True,a+b+c)
