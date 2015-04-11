__author__ = 'neliko'


class Lion:
    def __init__(self, state, table):
        if state == "":
            raise Exception('Empty initial state')
        self.state = state
        self.action = ""
        self.table = table


    def isKnowObject(self, input_object):
        if (self.state, input_object) in self.table:
            return True
        else:
            return False

    def view(self, input_object):
        self.action = self.table[(self.state, input_object)][1]
        new_state = self.table[(self.state, input_object)][0]
        if new_state is not None:
            self.state = new_state


if __name__ == '__main__':

    table = {
        ("hungry", "antelope"): ("fed", "eat"),
        ("hungry", "hunter"): (None, "run"),
        ("hungry", "tree"): (None, "sleep"),
        ("fed", "antelope"): ("hungry", "sleep"),
        ("fed", "hunter"): ("hungry", "run"),
        ("fed", "tree"): ("hungry", "see")
    }
    lion = Lion("fed", table)
    print("Лев сыт")
    while True:
        print('Выберите один из объектов:\n antelope, hunter, tree')
        print('Введите объект или exit для выхода')
        data = input()
        if data == 'exit':
            break
        else:
            print("Реакция Льва:")
            print("I", lion.state, "and I see", data)
            if lion.isKnowObject(data):
                lion.view(data)
                print("Now my action is", lion.action, "and my state is", lion.state, "\n")
            else:
                print("I don't know what is it!\n")

