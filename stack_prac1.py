# 연습문제 - 수식의 괄호 유효성 검사
from stack import *

S = LinkedListStack()

while True:
    string = input("수식(-1 입력으로 종료): ")
    if string == '-1':
        break
    string = string.replace(" ", "")

    for x in string:
        if x == '(' or x == '{' or x == '[':
            S.push(x)
        if x == ')' or x == '}' or x == ']':
            if S.isEmpty():
                print("isEmpty")
                break
            elif x == ')' and S.peek() == '(':
                print("is )")
                S.pop()
            elif x == '}' and S.peek() == '{':
                print("is }")
                S.pop()
            elif x == ']' and S.peek() == '[':
                print("is ]")
                S.pop()
    if S.size() > 0:
        print("유효하지 않은 수식")
    else:
        print("유효한 수식")