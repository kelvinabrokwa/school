from Deque import Deque

class Stack:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return str(self._dq)

  def __len__(self):
    return len(self._dq)

  def push(self, val):
    self._dq.push_front(val)

  def pop(self):
    return self._dq.pop_front()

  def peek(self):
    return self._dq.peek_front()

if __name__ == '__main__':
  success = True

  s = Stack()

  adds = range(10)
  for i in adds:
    s.push(i)

  if str(s) != '[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]':
    print('ERROR: incorrect string formatting')
    success = False

  if s.pop() != adds[len(adds) - 1]:
    print('ERROR: pop does not work')
    success = False
  if s.peek() != adds[len(adds) - 2]:
    print('ERROR: peek does not work and pop does not work')
    success = False
  while len(s) != 0:
    s.pop()
  try:
    s.pop()
  except:
    print('ERROR: pop does not return expected value')
    success = False

  print('ALL TESTS PASSED!' if success else 'FAILURE')


