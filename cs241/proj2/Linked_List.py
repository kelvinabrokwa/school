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


class Poly_Val:

  def __init__(self, coef, exp):
    self._coefficient = coef
    self._exponent = exp

  def get_coefficient(self):
    return self._coefficient

  def get_exponent(self):
    return self._exponent

  def __str__(self):
    return str(self._coefficient) + 'x^' + str(self._exponent)

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods ignore your
  # requests when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location?

  # linked list tests

  # Tests for empty list
  ll = Linked_List()
  ll.get_element_at(1)
  print('OK: getting elements from an empty list does not throw')
  ll.remove_element_at(1)
  print('OK: remove elements from an empty list does not throw')

  # Test that inserting and removing from invalid indices does not affect list
  ll = Linked_List()
  for i in range(0, 4):
    ll.append_element(i)
  ll_state = ll.__str__()
  ll.insert_element_at(1, 20)
  if ll_state == ll.__str__():
    print('OK: inserting element at invalid index leaves the list unchanged')
  else:
    print('ERROR: inserting element at invalid index DOES NOT leave the list unchanged')
  ll.remove_element_at(20)
  if ll_state == ll.__str__():
    print('OK: removing element at invalid index leaves the list unchanged')
  else:
    print('ERROR: removing element at invalid index DOES NOT leave the list unchanged')

  # Test list length
  ll = Linked_List()
  for i in range(0, 4):
    ll.append_element(i)
    if len(ll) == i + 1:
      print('OK: list size increases with append call')
    else:
      print('ERROR: list size DOES NOT increases with append call')
  ll = Linked_List()
  for i in range(0, 4):
    ll.insert_element_at(i, i)
    if len(ll) == i + 1:
      print('OK: list size increases with insert_element_at calls')
    else:
      print('ERROR: list size DOES NOT increase with insert_element_at calls')
  length = 4
  for i in range(0, 4):
    ll.remove_element_at(0)
    length -= 1
    if len(ll) ==  length:
      print('OK: list size decreases with remove_element_at calls')
    else:
      print('ERROR: list size DOES NOT decrease with remove_element_at calls')



  # Test constructor
  ll = Linked_List()
  if len(ll) == 0:
    print('OK: list initiates with a length of 0')
  else:
    print('ERROR: list DOES NOT initiates with a length of 0')

  # Test get_element_at and append methods
  ll = Linked_List()
  original_1 = 1
  ll.append_element(original_1)
  result = ll.get_element_at(0)
  if result == original_1:
    print('OK: data appended to an empty list is at index 0')
  else:
    print('ERROR: data appended to an empty list is NOT at index 0')
  original_2 = 2
  ll.append_element(original_2)
  result = ll.get_element_at(len(ll) - 1)
  if result == original_2:
    print('OK: data appended to a list is at the end of the list')
  else:
    print('ERROR: data appended to a list is not at the end of the list')

  # Test get_element_at
  ll = Linked_List()
  for i in range(0, 10):
    ll.append_element(i)
  for i in range(0, len(ll)):
    if i == ll.get_element_at(i):
      print('OK: get_element at return the right element at index: ' + str(i))
    else:
      print('ERROR: get_element at DOES NOT return the right element at index: ' + str(i))

  # Test insert element at
  ll = Linked_List()
  for i in range(0, 10):
    ll.append_element(1)
  new_val = 100
  ll.insert_element_at(new_val, 5)
  if ll.get_element_at(5) == new_val:
    print('OK: get_element_at returns the value inserted at that index')
  else:
    print('ERROR: get_element_at DOES NOT returns the value inserted at that index')

  # Test __str__ method
  ll = Linked_List()
  expected = '[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]'
  for i in range(0, 10):
    ll.append_element(i)
  if ll.__str__() == expected:
    print('OK: print string correctly formatted')
  else:
    print('ERROR: print string IS NOT correctly formatted')

  # Test remove_element_at method
  ll = Linked_List()
  for i in range(0, 10):
    ll.append_element(i)
  idx = 5
  elem = ll.get_element_at(idx + 1)
  ll.remove_element_at(idx)
  if ll.get_element_at(idx) == elem:
    print('OK: remove_element_at works as expected')
  else:
    print('ERROR: remove_element_at does not work as expected')

  # The following code should appear after your tests for your
  # linked list class.

  p1 = Linked_List()
  p1.append_element(Poly_Val(10,1012))
  p1.append_element(Poly_Val(5,14))
  p1.append_element(Poly_Val(1,0))
  p2 = Linked_List()
  p2.append_element(Poly_Val(3,1990))
  p2.append_element(Poly_Val(-2,14))
  p2.append_element(Poly_Val(11,1))
  p2.append_element(Poly_Val(5,0))

  # here, create the Poly_Val objects that should comprise p3
  # and add them to the list. Make sure that p3 is constructed
  # correctly regardless of the contents of p1 and p2. Try
  # building different polynomials for p1 and p2 and ensure that
  # they sum correctly.

  p3 = Linked_List()
  for i in range(0, len(p1)):
    p3.append_element(p1.get_element_at(i))

  for i in range(0, len(p2)):
    itp = p2.get_element_at(i)
    p3_idx = 0
    p3_curr = p3.get_element_at(p3_idx)
    if itp.get_exponent() > p3_curr.get_exponent():
      p3.insert_element_at(itp, 0)
      continue
    while p3_idx < len(p3) and p3.get_element_at(p3_idx + 1).get_exponent() > itp.get_exponent():
      p3_idx += 1
      p3_curr = p3.get_element_at(p3_idx)

    if p3.get_element_at(p3_idx + 1).get_exponent() == itp.get_exponent():
      coeff = p3.get_element_at(p3_idx + 1).get_coefficient() + itp.get_coefficient()
      expo = p3.get_element_at(p3_idx + 1).get_exponent()
      new_val = Poly_Val(coeff, expo)
      p3.remove_element_at(p3_idx + 1)
      p3.insert_element_at(new_val, p3_idx + 1)
    elif p3_curr.get_exponent() > itp.get_exponent():
      new_val = Poly_Val(itp.get_coefficient(), itp.get_exponent())
      p3.insert_element_at(new_val, p3_idx + 1)
    elif p3_idx == len(p3):
      new_val = Poly_Val(itp.get_coefficient(), itp.get_exponent())
      p3.append_element(new_val)

  # test p3
  p3_expected = ['3x^1990', '10x^1012', '3x^14', '11x^1', '6x^0']
  for i in range (0, len(p3)):
    if str(p3.get_element_at(i)) == str(p3_expected[i]):
      print('OK: Element at ' + str(i) + ' of p3 is correct')
    else:
      print('Error: element at ' + str(i) + ' of p3 is incorrect')