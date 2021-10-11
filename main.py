#1st task (complete)
el_list = [1, 2, 3, 8]

class Stack:

    def __init__(self, el_list):
        self.el_list = el_list

    def isEmpty(self):
        if not self.el_list:
            return True
        else:
            return False

    def push(self, new_element):
        self.el_list.append(new_element)

    def pop(self):
        pop_element = self.el_list.pop()
        return pop_element

    def peek(self):
        peek_element = self.el_list[-1]
        return peek_element

    def size(self):
        return(len(self.el_list))


if __name__ =='__main__':
    obj = Stack(el_list)
    print(obj.peek())
