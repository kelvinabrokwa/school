from Deque import Deque

class Queue:

  def __init__(self):
    self._dq = Deque()

  def __str__(self):
    return str(self._dq)

  def __len__(self):
    return len(self._dq)

  def enqueue(self, val):
    self._dq.push_back(val)

  def dequeue(self):
    return self._dq.pop_front()

if __name__ == '__main__':
  success = True

  q = Queue()

  data = list(range(10))

  for i in data:
    q.enqueue(i)

  if str(q) != '[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]':
    print('ERROR: incorrect string formatting')
    success = False

  if len(q) != len(data):
    print('ERROR: length does not return the appropriate length')
    success = False

  for i in range(len(q)):
    if q.dequeue() != data[i]:
      print('ERROR: dequeue does not return expected result')
      success = False

  try:
    q.dequeue()
  except:
    print('ERROR: dequeueing from empty queue throws')
    success = False

  print('ALL TESTS PASSED!' if success else 'FAILURE')