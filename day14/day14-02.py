"""
큐
"""

'''
1. 큐
큐는 양쪽이 뚫려있는 기다란 통에서 한쪽은 데이터를 삽입하고 한쪽은 데이터를 삭제하는 자료구조
스택이 후입선출 (LIFO) 구조였다면, 큐는 먼저 들어간 데이터가 먼저 나오는
FIFO 구조
'''

'''
2. 큐의 메소드
-맨 뒤로 데이터를 삽입 :enqueue
-맨 앞의 데이터를 빼기 :dequeue
-맨 앞의 데이터를 빼지않고 조회: peek
-현재 큐에 데이터가 있는지 확인: isEmpty
'''

class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        """
        큐에 데이터가 없는지 확인

        :return:
        """
        #is_empty = False 웬만하면 변수를 선언해서 사용하는게 좋다
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self,data):
        """
        맨 뒤에 데이터를 삽입
        :param data:
        :return:
        """
        self.queue.append(data)

    def dequeue(self):
        """
        맨 앞의 데이터를 빼는 함수
        :return:
        """
        if self.isEmpty():
            print('Queue Is Empty')
        else:
            self.queue.pop(0)

    def peek(self):
        """
        맨 앞의 데이터를 빼지않고 반환해주는 함수
        :return:
        """
        if self.isEmpty():
            print('Queue is Empty')
        else:
           return self.queue[0]

queue = Queue()

queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(8)

print(queue.queue)
print(queue.peek())
print(queue.queue)

queue.dequeue()

print(queue.isEmpty())