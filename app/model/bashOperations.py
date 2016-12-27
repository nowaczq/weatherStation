from commands import *

class BashOperations():

    def __init__(self):
        pass

    def do_bash_script(self,script):
        state,text =  getstatusoutput(script)
        result_list = []
        result_list.append(text)
        tmp = result_list[0].split('\n')
        for t in tmp:
            print t
        result_list = []
        for t in tmp:
            result_list.append({"script" : t})
        return result_list
