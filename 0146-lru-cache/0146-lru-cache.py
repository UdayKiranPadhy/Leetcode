class Node():
    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.cache = {}
        self.left.next =self.right
        self.right.prev = self.left
    
    def remove(self,node):
        pre , nxt = node.prev , node.next
        pre.next , nxt.prev = nxt , pre
    
    def insert(self,node):
        prev , next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev , node.next = prev , next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
