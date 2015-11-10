from Linked_List import Linked_List

class Deque:

  def __init__(self):
    self._list = Linked_List()

  def __str__(self):
    return str(self._list)

  def __len__(self):
    return len(self._list)

  def push_front(self, val):
    self._list.insert_element_at(val, 0)
  
  def pop_front(self):
    if len(self._list) < 1:
      return
    item = self._list.get_element_at(0)
    self._list.remove_element_at(0)
    return item

  def peek_front(self):
    return self._list.get_element_at(0)

  def push_back(self, val):
    self._list.append_element(val)
  
  def pop_back(self):
    if len(self._list)  < 1:
      return
    idx = len(self._list) - 1
    item = self._list.get_element_at(idx)
    self._list.remove_element_at(idx)
    return item

  def peek_back(self):
    return self._list.get_element_at(len(self._list) - 1)

if __name__ == '__main__':
  deq = Deque()
  success = True
  # test push front
  d1 = 1
  d2 = 2
  d3 = 3
  deq.push_front(d1)
  deq.push_front(d2)
  deq.push_back(d3)
  if len(deq) != 3:
    print('ERROR with len')
    success = False
  if deq.peek_front() != d2:
    print('ERROR: push front doesn\'t work')
    success = False
  if deq.peek_back() != d3:
    print('ERROR: peek back doesn\'t work')
    success = False
  if deq.pop_front() != d2:
    print('ERROR: pop front does not work')
    success = False
  if deq.peek_front() != d1:
    print('ERROR: pop front still does not work')
    success = False
  if deq.pop_back() != d3:
    print('ERROR: pop back does not work')
    success = False

  while len(deq) != 0:
    deq.pop_back()

  try:
    deq.pop_back()
  except:
    print('ERROR: popping from empty deque throws')
    success = False

  print('ALL TESTS PASSED!' if success else 'FAILURE')
