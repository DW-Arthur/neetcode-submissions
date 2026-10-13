class Node:

  def __init__(self, val: int):
    self.val = val
    self.next = None
    self.prev = None


class MyCircularQueue:

  def __init__(self, k: int):
    self.capacity = k
    self.size = 0

    # Two sentinels (bookends)
    self.left = Node(0)
    self.right = Node(0)
    self.left.next = self.right
    self.right.prev = self.left

    # Tracks the most recently added node
    # When empty, the "last added node" is just self.left
    self.last_added = self.left

  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False

    node = Node(value)

    # 1. Wire the new node OUTWARD:
    # Placed directly to the right of self.last_added,
    # and directly to the left of self.right
    node.prev = self.last_added
    node.next = self.right

    # 2. Wire neighbors INWARD:
    self.last_added.next = node
    self.right.prev = node

    # 3. Update pointer to mark this new node as the most recently added
    self.last_added = node
    self.size += 1
    return True

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False

    # Oldest node is always directly after self.left
    target = self.left.next

    # Bypass target
    self.left.next = target.next
    target.next.prev = self.left

    self.size -= 1

    # If we just removed the only item, reset last_added back to self.left
    if self.size == 0:
      self.last_added = self.left

    return True

  def Front(self) -> int:
    if self.isEmpty():
      return -1
    return self.left.next.val

  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    return self.last_added.val

  def isEmpty(self) -> bool:
    return self.size == 0

  def isFull(self) -> bool:
    return self.size == self.capacity