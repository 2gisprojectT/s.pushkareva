__author__ = 'neliko'

class Lion:
    input_object=""
    def __init__(self):
        self.state="fed"
        self.action=""
        self.table={
            ("hungry","antilope"):("fed","eat"),
            ("hungry","hunter"):(None,"run"),
            ("hungry","tree"):(None,"sleep"),
            ("fed","antilope"):("hungry","sleep"),
            ("fed","hunter"):("hungry","run"),
            ("fed","tree"):("hungry","see")
        }
    def find_obj(self,input_object):
        if((self.state,input_object) in self.table):
            self.input_object=input_object
            return True
        else:
            return False


    def view(self,input_object):
        if(self.find_obj(input_object)):
            print ("I",self.state, "and I see",self.input_object)
            self.newData()
            print ("Now my action is", self.action, "and my state is", self.state,"\n")
        else:
            print ("I don't know what is it!\n")

    def get_state(self):#next state
        return self.table[(self.state,self.input_object)][0]

    def get_action(self):#action
        return self.table[(self.state,self.input_object)][1]

    def newData(self):
        self.action=self.get_action()
        new_state=self.get_state()
        if(new_state is not None):
            self.state=new_state
        return


if __name__ == '__main__':

    # Initialization
   lion=Lion()
   print("Лев сыт")
   while True:

        print('Выберите один из объектов:\n antilope, hunter, tree')
        print('Введите объект или exit для выхода')
        data = input()
        if data == 'exit':
            break
        else:
            print("Реакция Льва:")
            lion.view(data)


