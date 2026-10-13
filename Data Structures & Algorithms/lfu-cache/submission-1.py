from collections import defaultdict


class Node:

  def __init__(self, key: int, value: int):
    self.key = key
    self.val = value
    self.count = 1
    self.next = None
    self.prev = None


class DoublyLinkedList:

  def __init__(self):
    self.left = Node(-1, -1)  # LRU sentinel
    self.right = Node(-1, -1)  # MRU sentinel
    self.left.next = self.right
    self.right.prev = self.left
    self.size = 0

  def insert(self, node: Node) -> None:
    """Insert right before self.right (MRU)."""
    prev = self.right.prev
    node.next = self.right
    node.prev = prev
    prev.next = node
    self.right.prev = node
    self.size += 1

  def remove(self, node: Node) -> None:
    """Unlink an arbitrary node in O(1)."""
    node.prev.next = node.next
    node.next.prev = node.prev
    self.size -= 1

  def pop_lru(self) -> Node:
    """Remove and return the least-recently used node."""
    lru = self.left.next
    self.remove(lru)
    return lru


class LFUCache:

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.size = 0
    self.min_freq = 0

    self.cache = {}  # key -> Node
    self.freq_map = defaultdict(
        DoublyLinkedList
    )  # count -> DoublyLinkedList bucket

  def _update_freq(self, node: Node) -> None:
    """Helper: bumps node's frequency and relocates it between buckets."""
    old_freq = node.count
    self.freq_map[old_freq].remove(node)

    # If the vacated bucket was the minimum frequency and is now empty,
    # the new global minimum frequency must increment by 1
    if (
        self.min_freq == old_freq
        and self.freq_map[old_freq].size == 0
    ):
      self.min_freq += 1

    node.count += 1
    self.freq_map[node.count].insert(node)

  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1

    node = self.cache[key]
    self._update_freq(node)
    return node.val

  def put(self, key: int, value: int) -> None:
    if self.capacity == 0:
      return

    # Case 1: Key already exists -> update value & frequency
    if key in self.cache:
      node = self.cache[key]
      node.val = value
      self._update_freq(node)
      return

    # Case 2: At capacity -> evict LRU node from min_freq bucket
    if self.size == self.capacity:
      evicted = self.freq_map[self.min_freq].pop_lru()
      del self.cache[evicted.key]
      self.size -= 1

    # Case 3: Insert brand-new node (starts at frequency 1)
    new_node = Node(key, value)
    self.cache[key] = new_node
    self.freq_map[1].insert(new_node)
    self.min_freq = 1
    self.size += 1