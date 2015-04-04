__author__ = 'neliko'


class Lion:
    input_object = ""

    def __init__(self, state, table):
        self.state = state
        self.action = ""
        self.table = table

    def find_obj(self, input_object):
        if (self.state, input_object) in self.table:
            self.input_object = input_object
            return True
        else:
            return False

    def view(self):
        self.action = self.table[(self.state, self.input_object)][1]
        new_state = self.table[(self.state, self.input_object)][0]
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
            if lion.find_obj(data):
                lion.view()
                print("Now my action is", lion.action, "and my state is", lion.state, "\n")
            else:
                print("I don't know what is it!\n")

