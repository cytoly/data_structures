from ..implementations.Stack import Stack


def is_pair(start: str, close: str):
    if start == "(" and close == ")":   return True
    elif start == "{" and close == "}": return True
    elif start == "[" and close == "]": return True
    return False


def are_balanced(exp: str) -> bool:
    stk = Stack(len(exp))
    for char in exp:
        if char in ['[', '{', '(']:
            stk.push(char)
        elif char in [']', '}', ')']:
            if not is_pair(stk.peek(), char):
                return False
            stk.pop()
    if stk.is_empty():
        return True
    return False


if __name__ == "__main__":
    print(are_balanced("(3+5)*510*((230+30)*1+30)")) # True
    print(are_balanced("[h, h, h]]")) # False
