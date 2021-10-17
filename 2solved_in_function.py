from main import Stack

brackets_line = '(((([{}]))))'
brackets_line = list(brackets_line)
brackets_list = []
stack_list = Stack(brackets_list)


def create_open_brackets_list():
    for el in brackets_line:
        if el == '(' or el == '[' or el == '{':
            stack_list.push(el)
            print("stack_list= ", stack_list)
        elif el == ')' or el == ']' or el == '}':
            if not stack_list:
                return f"Несбалансировано. "
            if not el:
                return f"Несбалансировано. "
            if stack_list:
                open_bracket = stack_list.pop()
                print("open_bracket= ", open_bracket)
            else:
                return f"Несбалансировано. el= {el}"
            if open_bracket == "(" and el == ")":
                continue
            if open_bracket == "[" and el == "]":
                continue
            if open_bracket == "{" and el == "}":
                continue
            if not el:
                return f"Несбалансировано. "
            else:
                return f"Несбалансировано. el= {el}"
    if stack_list:
        return "Несбалансировано"
    return "Сбалансировано"


create_open_brackets_list()
