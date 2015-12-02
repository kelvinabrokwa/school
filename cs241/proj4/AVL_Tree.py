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
    self._root = self._balance(self._insert_element_at(self._root, value))

  def _insert_element_at(self, node, value):
    if node == None:
      return self._AVL_Node(value)
    elif value < node._value:
      node._left = self._balance(self._insert_element_at(node._left, value))
      return node
    elif value > node._value:
      node._right = self._balance(self._insert_element_at(node._right, value))
      return node

  def remove_element(self, value):
    # Remove the value specified from the tree, ensuring that
    # the tree remains balanced after the operation. Your solution
    # must be recursive. This will involve the introduction of
    # additional private methods.
    node = find(value)
    self._root = self._balance(self._remove_from(self._root))

  def _remove_from(self, node, value):
    if node._left == None and node._right == None:
      return None
    elif node._left == None:
      return self._balance(node._right)
    elif node._right == None:
      return self._balance(node.left)
    else:
      curr = node._right
      while curr._left._left != None:
        curr = curr._left
      n = curr._left
      curr._left = None
      n._right = node._right
      n._left = node._left
      return self._balance(n)


  def _find(self, value):
    curr = self._root
    while True:
      if curr == None:
        return None
      elif value == curr._value:
        return curr
      elif value < curr._value:
        curr = curr._left
      elif value > curr._value:
        curr = curr._right


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
    elif self._get_balance(node) == 2:
      pass
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
    return '[ ' + ''.join([ str(x) + ', ' for x in result  ]) + ']'

  def _in_order(self, node, result):
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
    return '[ ' + ''.join([ str(x) + ', ' for x in result  ]) + ']'

  def _pre_order(self, node, result):
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
    return '[ ' + ''.join([ str(x) + ', ' for x in result  ]) + ']'

  def _post_order(self, node, result):
    if node._left != None:
      self._post_order(node._left, result)

    if node._right != None:
      self._post_order(node._right, result)

    result.append(node._value)

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
  for i in range(5, 0, -1):
    t.insert_element(i)
  print(t.post_order())


