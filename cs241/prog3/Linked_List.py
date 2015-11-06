class Linked_List:

  class _Node:

    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      self.value = val
      self.prev = None
      self.next = None


  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    self._length = 0
    self._header = self._Node(None)
    self._trailer = self._Node(None)
    self._header.next = self._trailer
    self._trailer.prev = self._header


  def __len__(self):
    # return the number of value-containing nodes in
    # this list.
    return self._length

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the tail position.
    new_node = self._Node(val)
    curr = self._header
    while curr.next is not self._trailer:
      curr = curr.next
    new_node.next = self._trailer
    new_node.prev = curr
    curr.next = new_node
    self._trailer.prev = new_node
    self._length += 1

  def insert_element_at(self, val, index):
    # assuming the head position is indexed 0, add a
    # node containing val at the specified index. If
    # the index is not a valid position within the list,
    # ignore the request. This method cannot be used
    # to add an item at the tail position.
    if self._length < index:
      return
    new_node = self._Node(val)
    curr = self._header
    i = 0
    while i != index:
      curr = curr.next
      i += 1
    new_node.next = curr.next
    new_node.prev = curr
    curr.next = new_node
    new_node.next.prev = new_node
    self._length += 1

  def remove_element_at(self, index):
    # assuming the head position is indexed 0, remove
    # and return the value stored in the node at the
    # specified index. If the index is invalid, ignore
    # the request.
    if self._length < index:
      return
    curr = self._header
    i = 0
    while i <= index:
      curr = curr.next
      i += 1
    curr.prev.next = curr.next
    curr.next.prev = curr.prev
    self._length -= 1

  def get_element_at(self, index):
    # assuming the head position is indexed 0, return
    # the value stored in the node at the specified
    # index, but do not unlink it from the list.
    if self._length < index:
      return
    curr = self._header
    i = 0
    while i <= index:
      curr = curr.next
      i += 1
    return curr.value

  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    output = '['
    curr = self._header.next
    while curr.next is not self._trailer:
      output += ' ' + str(curr.value) + ','
      curr = curr.next
    output += ' ' + str(curr.value)
    output += ' ]'
    return output