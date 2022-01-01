"""
트리

"""

'''

1. 트리
- 하나의 뿌리에서 위로 뻗어 나가는 형상
- 트리는 자식도 트리고 또 그 자식도 트리
- 여러 노드가 한 노드를 가리킬 수 없는 구조!

[용어]
루트 노드 : 부모가 없는 최상위 노드, 트리의 시작점
노드 : 마디
부모 노드 : 어떤 노드와 링크로 연결되어 있는 상위 노드
자식 노드 : 어떤 노드와 링크로 연결되어 있는 하위 노드
리프 노드 : 자식이 없는 노드
깊이 : 루트에서 시작해 특정 노드에 도달하기 위해 거치는 간선의 수
레벨 : 노드와 루트사이의 간선의 수 + 1 또는 특정 깊이의 노드들의 집합
간선 : 한 노드와 다른 노드 사이의 연결선
'''

'''
2. 정 이진 트리
- 모든 노드가 0개 또는 2개의 자식 노드를 갖는다.
'''

'''
3. 완전 이진 트리
-마지막 레벨을 제외하고 모든 레벨이 완전히 채워져있으며,
마지막 레벨의 모든 노드는 가장 왼쪽부터 채워져있다.
'''

'''
4. 포화 이진 트리 
- 모든 노드가 2개의 노드를 갖고 있으며, 모든 리프 노드가 동일한 깊이 또는 레벨을 갖는다.
- 가장 완벽한 유형의 트리!
'''

'''
5. 트리 노드 구현
- 트리 노드 클래스는 인스턴스 변수가 3개 입니다.
-- data : 데이터를 담는 인스턴스 변수
-- left :  왼쪽 자식 노드를 가리킴
-- right : 오른쪽 자식 노드를 가리킴

'''

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data




class BinarySerachTree:

    def __init__(self):
        self.root = None

    '''
    5.1 조회 함수
    '''

    def print(self):
        self._print_tree(self.root)

    '''
    5.2 조회 재귀 함수
    '''
    def _print_tree(self,node):
        if node is not None:
            print(node.data)
            if node.left is not None:
                self._print_tree(node.left)
            if node.right is not None:
                self._print_tree(node.right)

    '''
    5.3 삽입 메소드
    삽입 메소드는 다음 사항을 고려해야 한다.
    -인수의 값을 상위 노드( 부모 노드)와 비교해야하고 이를 기준으로
    작으면 -> 왼쪽
    크면-> 오른쪽
    
    '''

    def insert(self,data):
        self.root = self._insert_value(self.root,data)
        return  self.root is not None

    def _insert_value(self,node, data):
        if node is None:
            node = Node(data)
        else:
            if data< node.data:
                node.left = self._insert_value(node.left,data)
            elif data > node.data:
                node.right = self._insert_value(node.right,data)
        return node

    '''
    5.4
    
    '''

    def find (self,key):
        return self._find_value(self.root,key)
    def _find_value(self,root,key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right,key)

    '''
    5.5 삭제 메소드
    삭제 메소드는 3개로 나누어진다.
    -자식이 없는 노드를 삭제할 때 -> 삭제
    - 자식이 하나만 있는 노드를 삭제할 때
    - 자식이 둘 다 있는 노드를 삭제할 때
    
    
    '''
    def delete(self,key):
        self.root,deleted = self._delete_value(self.root,key)
        return deleted
    def _delete_value(self,node,key):
        if node is None:
            return node, False

        deleted = False
        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            deleted =True

            # 삭제할 노드가 자식이 두개인 경우
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent,child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 자식 노드가 하나일 경우 해당 노드와 교체

            elif node.left or node.right:
                node = node.left or node.right
            # 자식 노드가 없을 경우 그냥 삭제
            else:
                node = None

        elif key < node.data:
            node.left, deleted = self._delete_value(node.left,key)
        else:
            node.right, deleted = self._delete_value(node.right,key)

        return node, deleted

arr = [10,5,3,15,19,6]
bst = BinarySerachTree()
for x in arr:
    bst.insert(x)

print(bst.find(15))
print(bst.find(17))

# 조회
# 항상 왼쪽을 바라보며 출력
print(bst.print())

bst.delete(15)
print(bst.print())