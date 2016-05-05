-- Kelvin Abrokwa-Johnson
-- PPL
-- Assignment 7
-- Proffessor Davis
-- This project is a program that conducts basic list operations in haskel
-- the expected output for each project is commented above each statement

list = [1,2,3,4,5]

main = do

  -- [1,2,3,4,5]
  print(list)

  -- 1
  print(head list)

  -- [2,3,4,5]
  print(tail list)

  -- 5
  print(last list)

  -- [1,2,3,4]
  print(init list)

  -- 4
  print(last (init list))

  -- True
  print(elem 3 list)

  -- 5
  print(length list)

  -- False
  print(null list)

  -- [5,4,3,2,1]
  print(reverse list)

  -- [1,2]
  print(take 2 list)

  -- [3,4,5]
  print(tail (tail list))

  -- least
  -- 1
  print(minimum list)

  -- 5
  print(maximum list)

  -- 15
  print(sum list)

  -- 120
  print(product list)

  -- [2,3,4,5,6]
  print(map (+ 1) list)

  -- [4,5]
  print(drop 3 list)

  -- False
  print(all even list)

  -- True
  print(any odd list)

  -- [1,2,3,4,5,6,7,8,9,10]
  print([1..10])

  -- "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  print(['A'..'Z'])

  -- [2,4,6,8,10,12,14,16,18,20]
  print([2,4..20])

  -- [0,0,0,0,0,0,0,0,0,0]
  print(replicate 10 0)

  -- "abc"
  print(['a','b']++['c'])

  -- [(1,'a'),(2,'b'),(3,'c')]
  print(zip [1..3] ['a'..'c'])

  -- ([1,2,3],"abc")
  print(unzip [(1,'a'),(2,'b'),(3,'c')])

  -- ["Hello","world"]
  print(words "Hello world")
