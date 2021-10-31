from main import Stack

brackets_line = '(((([{}]))))'
brackets_line = list(brackets_line)
brackets_list = []
stack_list = Stack(brackets_list)


def create_open_brackets_list():
    for el in brackets_line:
        if el == '(' or el == '[' or el == '{':
            stack_list.push(el)
            print("stack_list= ", stack_list.el_list)
        elif el == ')' or el == ']' or el == '}':
            if stack_list.isEmpty():
                return f"Несбалансировано. size = 0"
            elif stack_list:
                open_bracket = stack_list.pop()
                if open_bracket == "(" and el == ")":
                    continue
                if open_bracket == "[" and el == "]":
                    continue
                if open_bracket == "{" and el == "}":
                    continue
    if stack_list:
        return "Несбалансировано"
    return "Сбалансировано"


print(create_open_brackets_list())
