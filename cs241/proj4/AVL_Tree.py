class AVL_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _AVL_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
      self._value = value
      self._left = None
      self._right = None


  def __init__(self):
    self._root = None


  def insert_element(self, value):
    # Insert the value specified into the tree, ensuring that
    # the tree remains balanced after the operation. Your solution
    # must be recursive. This will involve the introduction of
    # additional private methods.
    self._root = self._insert_element_at(self._root, value)


  def _insert_element_at(self, node, value):
    if node == None:
      return self._AVL_Node(value)
    elif value < node._value:
      node._left = self._balance(self._insert_element_at(node._left, value))
      return self._balance(node)
    elif value > node._value:
      node._right = self._balance(self._insert_element_at(node._right, value))
      return self._balance(node)
    else:
      return node


  def remove_element(self, value):
    # Remove the value specified from the tree, ensuring that
    # the tree remains balanced after the operation. Your solution
    # must be recursive. This will involve the introduction of
    # additional private methods.
    self._root = self._remove_from(self._root, value)


  def _remove_from(self, node, value):
    if node == None:
      return node
    elif node._value == value: # found the value
      if node._left == None and node._right == None: # no children of node to remove
        return None
      elif node._left == None: # item to remove only has right child
        return self._balance(node._right)
      elif node._right == None: # item to remove only has left child
        return self._balance(node._left)
      else: # node to remove has two children, replace it with its smallest right child
        node._value = self._get_min(node._right)._value
        node._right = self._balance(self._remove_min(node._right))
        return self._balance(node)
    elif node._value > value:
      node._left = self._remove_from(node._left, value)
      return self._balance(node)
    else:
      node._right = self._remove_from(node._right, value)
      return self._balance(node)


  def _get_min(self, node):
    if node._left == None:
      return node
    else:
      return self._get_min(node._left)


  def _remove_min(self, node):
    if node._left == None:
      return node._right
    else:
      node._left = self._remove_min(node._left)
      return node


  def _balance(self, node):
    if node == None:
      return None
    elif self._get_balance(node) < 2 and self._get_balance(node) > -2:
      return node
    balance = self._get_balance(node)
    if balance == -2:
      if self._get_balance(node._left) == -1: # left-left
        return self._rotate_right(node)
      else:                                   # left-right
        node._left = self._rotate_left(node._left)
        return self._rotate_right(node)
    elif balance == 2:
      if self._get_balance(node._right) == 1: # right-right
        return self._rotate_left(node)
      else:                                   # right-left
        node._right = self._rotate_right(node._right)
        return self._rotate_left(node)


  def _rotate_right(self, node):
    l = node._left
    node._left = l._right
    l._right = node
    return l


  def _rotate_left(self, node):
    r = node._right
    node._right = r._left
    r._left = node
    return r


  def _get_balance(self, node):
    return self._get_height(node._right) - self._get_height(node._left)


  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    result = []
    self._in_order(self._root, result)
    return self._stringify(result)


  def _in_order(self, node, result):
    if node == None:
      return

    if node._left != None:
      self._in_order(node._left, result)

    result.append(node._value)

    if node._right != None:
      self._in_order(node._right, result)


  def pre_order(self):
    # Construct and return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    result = []
    self._pre_order(self._root, result)
    return self._stringify(result)


  def _pre_order(self, node, result):

    if node == None:
      return

    result.append(node._value)

    if node._left != None:
      self._pre_order(node._left, result)

    if node._right != None:
      self._pre_order(node._right, result)


  def post_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    result = []
    self._post_order(self._root, result)
    return self._stringify(result)


  def _post_order(self, node, result):

    if node == None:
      return

    if node._left != None:
      self._post_order(node._left, result)

    if node._right != None:
      self._post_order(node._right, result)

    result.append(node._value)


  def _stringify(self, li):
    output = '[ '
    for i, val in enumerate(li):
      output += str(val) + ( ', ' if i != len(li) - 1 else ' ' )
    output += ']'
    return output


  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1.
    return self._get_height(self._root)


  def _get_height(self, node):
    if node == None:
      return 0
    return 1 + max(self._get_height(node._left), self._get_height(node._right))


  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  t = AVL_Tree()

  # Test empty tree formatting
  if t.in_order() != '[ ]':
    print('FAILED: empty string formatting for in order incorrect')
  if t.pre_order() != '[ ]':
    print('FAILED: empty string formatting for pre order incorrect')
  if t.post_order() != '[ ]':
    print('FAILED: empty string formatting for post order incorrect')

  # Test insertions, heights and string formatting
  t.insert_element(1)
  if t.pre_order() != '[ 1 ]':
    print('FAILED: incorrect pre order after insertion -> 1')
  if t.post_order() != '[ 1 ]':
    print('FAILED: incorrect post order after insertion -> 1')
  if t.get_height() != 1:
    print('FAILED: incorrect height')

  t.insert_element(2)
  if t.pre_order() != '[ 1, 2 ]':
    print('FAILED: incorrect pre order after insertion -> 2')
  if t.post_order() != '[ 2, 1 ]':
    print('FAILED: incorrect post order after insertion -> 2')
  if t.get_height() != 2:
    print('FAILED: incorrect height')

  t.insert_element(3)
  if t.pre_order() != '[ 2, 1, 3 ]':
    print('FAILED: incorrect pre order after insertion -> 3')
  if t.post_order() != '[ 1, 3, 2 ]':
    print('FAILED: incorrect post order after insertion -> 3')
  if t.get_height() != 2:
    print('FAILED: incorrect height')

  t.insert_element(4)
  if t.pre_order() != '[ 2, 1, 3, 4 ]':
    print('FAILED: incorrect pre order after insertion -> 4')
  if t.post_order() != '[ 1, 4, 3, 2 ]':
    print('FAILED: incorrect post order after insertion -> 4')
  if t.get_height() != 3:
    print('FAILED: incorrect height')

  t.insert_element(5)
  if t.pre_order() != '[ 2, 1, 4, 3, 5 ]':
    print('FAILED: incorrect pre order after insertion -> 5')
  if t.post_order() != '[ 1, 3, 5, 4, 2 ]':
    print('FAILED: incorrect post order after insertion -> 5')
  if t.get_height() != 3:
    print('FAILED: incorrect height')

  if t.in_order() != '[ 1, 2, 3, 4, 5 ]':
    print('FAILED: incorrect in order')

  # Insert element already in tree
  t.insert_element(5)
  if t.pre_order() != '[ 2, 1, 4, 3, 5 ]':
    print('FAILED: incorrect pre order after insertion of existing value-> 5')
  if t.post_order() != '[ 1, 3, 5, 4, 2 ]':
    print('FAILED: incorrect post order after insertion of existing value -> 5')
  if t.get_height() != 3:
    print('FAILED: incorrect height')


  # Remove element that is not in the tree
  try:
    t.remove_element(10)
  except:
    print('FAILED: removing element not in tree threw')
  if t.pre_order() != '[ 2, 1, 4, 3, 5 ]':
    print('FAILED: incorrect pre order after insertion of existing value-> 5')
  if t.post_order() != '[ 1, 3, 5, 4, 2 ]':
    print('FAILED: incorrect post order after insertion of existing value -> 5')
  if t.get_height() != 3:
    print('FAILED: incorrect height')


  # Test all deletion types
  t = AVL_Tree()

  for i in range(1, 9):
    t.insert_element(i)
  t.insert_element(0)

  # Delete node with one right child
  t.remove_element(7)
  if t.pre_order() != '[ 4, 2, 1, 0, 3, 6, 5, 8 ]':
    print('FAILED: incorrect pre order after deletion')
  if t.post_order() != '[ 0, 1, 3, 2, 5, 8, 6, 4 ]':
    print('FAILED: incorrect post order after deletion')

  # Delete node with one left child
  t.remove_element(1)
  if t.pre_order() != '[ 4, 2, 0, 3, 6, 5, 8 ]':
    print('FAILED: incorrect pre order after deletion')
  if t.post_order() != '[ 0, 3, 2, 5, 8, 6, 4 ]':
    print('FAILED: incorrect post order after deletion')

  # Delete node with two children
  t.remove_element(2)
  if t.pre_order() != '[ 4, 3, 0, 6, 5, 8 ]':
    print("FAILED: incorrect pre order after deletion")
  if t.post_order() != '[ 0, 3, 5, 8, 6, 4 ]':
    print('FAILED: incorrect post order after deletion')

  # Delete leaf node
  t.remove_element(5)
  if t.pre_order() != '[ 4, 3, 0, 6, 8 ]':
    print('FAILED: incorrect pre order after deletion')
  if t.post_order() != '[ 0, 3, 8, 6, 4 ]':
    print('FAILED: incorrect post order after deletion')