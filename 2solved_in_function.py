brackets_line = '((())'
brackets_line = list(brackets_line)


# print(brackets_line)


def create_open_brackets_list():
    brackets_list = []
    for el in brackets_line:
        if el == '(' or el == '[' or el == '{':
            brackets_list.append(el)
        elif el == ')' or el == ']' or el == '}':
            if brackets_list:
                open_bracket = brackets_list.pop()
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
    if brackets_list:
        return "Несбалансировано"
    return "Сбалансировано"


print(create_open_brackets_list())
