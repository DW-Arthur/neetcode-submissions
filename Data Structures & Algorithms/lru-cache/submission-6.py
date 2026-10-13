class Node:

  def __init__(self, key: int, value: int):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None


class LRUCache:

  def __init__(self, capacity: int):
    self.size = 0
    self.capacity = capacity
    self.LFU = Node(-1, 0)
    self.MFU = Node(-1, 0)
    self.LFU.next = self.MFU
    self.MFU.prev = self.LFU
    self.cache = {}

  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1

    node = self.cache[key]
    self.remove(node)
    self.insert(node)
    return node.value

  def remove(self, node: Node) -> None:
    previous = node.prev
    nxt = node.next
    previous.next = nxt
    nxt.prev = previous

  def insert(self, node: Node) -> None:
    previous = self.MFU.prev

    # Wire node outward
    node.prev = previous
    node.next = self.MFU

    # Wire neighbors inward
    previous.next = node
    self.MFU.prev = node

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      node = self.cache[key]
      node.value = value
      self.remove(node)
      self.insert(node)
    else:
      if self.size == self.capacity:
        # Evict LRU node (right next to sentinel self.LFU)
        lru_node = self.LFU.next
        self.remove(lru_node)
        del self.cache[lru_node.key]
        self.size -= 1

      new_node = Node(key, value)
      self.cache[key] = new_node
      self.insert(new_node)
      self.size += 1