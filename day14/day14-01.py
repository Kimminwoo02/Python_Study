"""

스택

"""

'''
1. 스택
-데이터의 삽입과 삭제가 데이터의 가장 끝쪽에서만 일어나는 자료구조
-가장 마지막에 삽입된 데이터가 가장 먼저 사용되거나 삭제
'''

'''
2. 스택의 메소드
-마지막에 데이터를 삽입 [push]
-마지막 데이터를 삭제 [pop]
-마지막 데이터를 삭제하지 않고 반환[top]
-현재 스택이 비어있는지 확인 [isEmpty]
'''

class Stack:

    def __init__(self):
        #리스트로 표현
        self.stack = []
    def push(self,data):
        """
        마지막에 데이터를 삽입
        :param data:
        :return:
        """
        self.stack.append(data)
    def isEmpty(self):
        """
        현재 스택이 비어있는지 확인

        :return:
        """
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty
    def pop(self):
        """
        마지막 데이터를 삭제

        """
        if self.isEmpty():
            # 비어있을경우 stack is empty를 출력
            print('Stack is Empty')
        else:
            self.stack.pop()
    def top(self):
        """
        마지막에 있는 데이터를 삭제하지 않고 반환
        :return:
        """
        if self.isEmpty():
            print('Stack is Empty')
        else:
            return self.stack[-1]

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print(stack.stack)
stack.pop()
stack.pop()
print(stack.stack)