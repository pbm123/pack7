import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, message,message2,message3):
        print("Sum="+str(message1+message2+message3))
        return(True,message1+message2+message3)
