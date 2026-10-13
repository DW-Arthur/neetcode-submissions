class Node:

  def __init__(self, val: int):
    self.val = val
    self.next = None
    self.prev = None


class MyCircularQueue:

  def __init__(self, k: int):
    self.size = 0
    self.capacity = k
    self.left = Node(0)
    self.right = Node(0)
    self.left.next = self.right
    self.right.prev = self.left

  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False

    # Insert right before self.right (MRU / Rear)
    node = Node(value)
    prev = self.right.prev

    node.next = self.right
    node.prev = prev
    prev.next = node
    self.right.prev = node

    self.size += 1
    return True

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False

    # Remove right after self.left (FIFO / Front)
    target = self.left.next
    nxt = target.next

    self.left.next = nxt
    nxt.prev = self.left

    self.size -= 1
    return True

  def Front(self) -> int:
    if self.isEmpty():
      return -1
    return self.left.next.val

  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    return self.right.prev.val

  def isEmpty(self) -> bool:
    return self.size == 0

  def isFull(self) -> bool:
    return self.size == self.capacity