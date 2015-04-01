class Lion:
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

    def view(self,obj):
         print "Now my state is", self.state

lion=Lion()
lion.start("fed")
lion.view("antilope")