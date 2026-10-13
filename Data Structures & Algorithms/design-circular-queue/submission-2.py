class Node:

  def __init__(self, val: int):
    self.val = val
    self.next = None
    self.prev = None


class MyCircularQueue:

  def __init__(self, k: int):
    self.capacity = k
    self.size = 0

    # Bookends of the queue
    self.left = Node(0)  # Front boundary
    self.right = Node(0)  # Back boundary

    # Start empty: left and right hold hands
    self.left.next = self.right
    self.right.prev = self.left

  def enQueue(self, value: int) -> bool:
    if self.isFull():
      return False

    node = Node(value)

    # Mental Model: Find the previously added node.
    # Because self.right sits at the very end,
    # the last added node is ALWAYS self.right.prev!
    last_added = self.right.prev

    # Slot the new node to the right of last_added, before self.right
    # 1. Wire new node outward
    node.prev = last_added
    node.next = self.right

    # 2. Wire neighbors inward
    last_added.next = node
    self.right.prev = node

    self.size += 1
    return True

  def deQueue(self) -> bool:
    if self.isEmpty():
      return False

    # FIFO: Remove the oldest node (the one right after self.left)
    oldest = self.left.next
    new_first = oldest.next

    self.left.next = new_first
    new_first.prev = self.left

    self.size -= 1
    return True

  def Front(self) -> int:
    if self.isEmpty():
      return -1
    return self.left.next.val

  def Rear(self) -> int:
    if self.isEmpty():
      return -1
    # The most recently added node is always right before self.right
    return self.right.prev.val

  def isEmpty(self) -> bool:
    return self.size == 0

  def isFull(self) -> bool:
    return self.size == self.capacity