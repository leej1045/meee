#  BSTNode
class BSTNode:          
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.left = None
        
        self.right = None
#이진탐색 트리 삽입, 삭제, 탐색 함수

def search_bst(n, key) :  #이진탐색 트리(순환함수)
    if n == None :
        return None
    elif key == n.key:
        return n
    elif key < n.key:      
        return search_bst(n.left, key)
    else:               
        return search_bst(n.right, key)

def search_bst_iter(n, key) :   #이진탐색 트리(반복함수)
    while n != None :       
        if key == n.key:      
            return n
        elif key < n.key:       
            n = n.left      
        else:        
            n = n.right       
    return None       

def search_value_bst(n, value) :  # 값을 이용한 탐색
    if n == None : return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value) 
    if res is not None :
        return res
    else :
        return search_value_bst(n.right, value)

def search_max_bst(n) :
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n) :
    while n != None and n.left != None:
        n = n.left
    return n



def insert_bst(r, n) :  #이진탐색 트리 삽입연산(노드 삽입): 순환구조 이용
    if n.key < r.key:
        if r.left is None :
            r.left = n
            return True
        else :
            return insert_bst(r.left, n)
    elif n.key > r.key :
        if r.right is None :
            r.right = n
            return True
        else :
            return insert_bst(r.right, n)
    else :        
        return False


def delete_bst_case1 (parent, node, root) :
    if parent is None:    
        root = None     
    else :
        if parent.left == node : 
            parent.left = None
        else :     
            parent.right = None

    return root          

def delete_bst_case2 (parent, node, root) :
    if node.left is not None :
        child = node.left
    else :
        child = node.right

    if node == root :
        root = child
    else :
        if node is parent.left : 
            parent.left = child
        else :
            parent.right = child

    return root

def delete_bst_case3 (parent, node, root) :
    succp = node
    succ = node.right
    while (succ.left != None) :
        succp = succ
        succ = succ.left

    if (succp.left == succ) :
        succp.left = succ.right
    else :
        succp.right = succ.right

    node.key = succ.key
    node.value= succ.value
    node = succ;      

    return root

def delete_bst (root, key) :
    if root == None : return None   

    parent = None   
    node = root        
    while node != None and node.key != key :
        parent = node
        if key < node.key : node = node.left
        else : node = node.right;

    if node == None : return None   
    if node.left == None and node.right == None:
        root = delete_bst_case1 (parent, node, root)
    elif node.left==None or node.right==None :
        root = delete_bst_case2 (parent, node, root)
    else :
        root = delete_bst_case3 (parent, node, root)
# inorder함수
def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)
# BSTMap

class BSTMap():     
    def __init__ (self):
        self.root = None

    def isEmpty (self): return self.root == None
    def clear(self): self.root = None       
    def size(self): return count_node(self.root)

    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def findMax(self): return search_max_bst(self.root)
    def findMin(self): return search_min_bst(self.root)

    def insert(self, key, value=None):
        n = BSTNode(key, value)  
        if self.isEmpty() :       
            self.root = n   
        else :          
            insert_bst(self.root, n) 

    def delete(self, key):   
        delete_bst (self.root, key)

    def display(self, msg = 'BSTMap :'):
        print(msg, end='')
        inorder(self.root)
        print()
map = BSTMap()
while True :
    command = input("삽입(i), 탐색(s), 삭제(d), 출력(p), 종료(q):  ")
    if command == 'i':
        name = input("친구의 이름: ")
        phone = input("친구의 전화번호: ")
        map.insert(name, phone)
    elif command == 's':
        name = input("친구의 이름: ")
        result = map.search(name)
        if result is None:
            print(f"{name} 등록되지 않은 친구입니다.")
        else:
            print(f"{name} 의 전화번호: {result.value}")
    elif command == 'd':
        name = input("친구의 이름: ")
        map.delete(name)
    elif command == 'p':
        print("내 전화번호부")
        map.display("--->")
       
    elif command == 'q' : break
    
    
