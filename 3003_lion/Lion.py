__author__ = 'neliko'

class Lion:
    obj=""
    def __init__(self):
        self.state=""
        self.action=""
        self.table={
            ("hungry","antilope"):("fed","eat"),
            ("hungry","hunter"):(None,"run"),
            ("hungry","tree"):(None,"sleep"),
            ("fed","antilope"):("hungry","sleep"),
            ("fed","hunter"):("hungry","run"),
            ("fed","tree"):("hungry","see")
        }
    def start(self,state):
        self.state=state

    def find_obj(self,obj):
        if((self.state,obj) in self.table):
            self.obj=obj
            return True
        else:
            return False


    def view(self,obj):
        if(self.find_obj(obj)):
            print ("I",self.state, "and I see",self.obj)
            self.newData()
            print ("Now my action is", self.action, "and my state is", self.state,"\n")
        else:
            print ("I don't know what is it!\n")

    def get_state(self):#next state
        return self.table[(self.state,self.obj)][0]
    def get_action(self):#action
        return self.table[(self.state,self.obj)][1]

    def newData(self):
        self.action=self.get_action()
        new_state=self.get_state()
        if(new_state is not None):
            self.state=new_state
        return

lion=Lion()
lion.start("fed")
lion.view("antilope")
lion.view("antilope")
lion.view("hunter")
lion.view("hunter")
lion.view("cat")
