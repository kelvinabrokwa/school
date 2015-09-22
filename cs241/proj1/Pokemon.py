class Score:

  def __init__(self, player_name):
    # The required attributes
    self._player_name = player_name
    self._current_score = 0
    self._current_level = 0
    self._current_multiplier = 1
    self._lives_remaining = 3

  # The required methods
  def add_points(self, amount):
    # implement this method by adding the number of points
    # specified by amount times the currentMultiplier value
    # to the currentScore. If the new score value should
    # result in the level changing, then change currentLevel.
    # return the new value of currentScore.
    self._current_score += amount * self._current_multiplier
    if self._current_score > (2**self._current_level * 10000) - 1:
      level = 0
      while self._current_score > (2**level * 10000) - 1 or self._current_score < ((2** (level - 1)) * 10000) - 1:
        level += 1
      self._current_level = level
      return self._current_score

  def subtract_points(self, amount):
    # reset currentMultiplier to 1. subtract the number of
    # points specified by amount from currentScore, and update
    # currentLevel if necessary.
    # return the new value of currentScore.
    self._current_multiplier = 1
    self._current_score -= amount
    if self._current_score < 0:
      self._current_score = 0
      self._current_level = 0
    elif self._current_score < (2**(self._current_level - 1) * 10000) - 1:
      level = self._current_level
      while self._current_score < (2**(level - 1) *10000) - 1:
        level -= 1
      self._current_level = level
    return self._current_score

  def get_player_name(self):
    # return the name of the player associated with this object.
    return self._player_name

  def get_multiplier(self):
    # return the current value of the multiplier attribute.
    return self._current_multiplier


  def increment_multiplier(self):
    # increase the value of currentMultiplier by one.
    # return the new value of currentMultiplier.
    self._current_multiplier += 1
    return self._current_multiplier

  def get_score(self):
    # return the current value of the score attribute.
    return self._current_score

  def get_level(self):
    # return the current value of the level attribute.
    return self._current_level

  def get_lives(self):
    # return the number of lives remaining.
   return self._lives_remaining

  def lose_life(self):
    # decrement the number of lives remaining. If, after you
    # have decremented the lives attributes, that attribute
    # has a positive value, return True, indicating play can
    # continue. If the number is zero, return false,
    # indicating that the game is over.
    self._lives_remaining -= 1
    return self._lives_remaining > 0

  def gain_life(self):
    # increase the current value of the lives attribute
    # by one.
    self._lives_remaining += 1

  def __str__(self):
    return self._player_name + ' SCORE: ' + str(self._current_score) +\
        ' LVL: '+ str(self._current_level) +\
        ' MULT: ' + str(self._current_multiplier) +\
        ' LIVES: ' + str(self._lives_remaining)

class Scoreboard:

  def __init__(self, capacity):
    self._capacity = capacity
    self._high_scores = [None] * capacity
    self._entries = 0

  def update(self, candidate_score):
    # if candidate_score has a score value higher than the
    # lowest score in the Scoreboard, add it at the correct position.
    if self._entries == 0:
      self._high_scores[0] = candidate_score
      self._entries += 1
    elif self._high_scores[self._entries] == None or candidate_score.get_score() > self._high_scores[self._entries]:
      self._high_scores[self._entries] = candidate_score
      if self._entries < self._capacity - 1:
        self._entries += 1
      self._sort()

  def _sort(self):
    for i in range(len(self._high_scores)):
      for j in range(i +1, len(self._high_scores)):
        if self._high_scores[j] != None and self._high_scores[j].get_score() > self._high_scores[i].get_score():
          tmp = self._high_scores[i]
          self._high_scores[i] = self._high_scores[j]
          self._high_scores[j] = tmp

  def print_scoreboard(self):
    # take advantage of the fact that the Score object implements
    # the __str__() method, and can therefore be passed directly to
    # print(). Use this to print the current score board.
    print(self.__str__())

  def __str__(self):
    output = " "
    for player in self._high_scores:
      if player != None:
        output += "Player Name: " + player.get_player_name() + ' - score: ' + str(player.get_score()) + '\n'
    return output

if __name__ == '__main__':
  # your test code goes here
  # Create multiple Score objects, 
  # Test the methods thoroughly.
  # Be careful not to make assumptions
  # about how the methods behave or what
  # order things happen in.
  #
  # Finally, create a Scoreboard instance and
  # add your score objects to it, printing it 
  # each time to ensure that they are ordered
  # correctly.
  s = Scoreboard(10)
  player1 = Score('p1')
  player2 = Score('p2')
  player3 = Score('p3')
  player4 = Score('p4')
  player1.add_points(20000)
  player2.add_points(10000)
  player3.add_points(80000)
  player4.add_points(40000)

  for i in [player1, player2, player3, player4]:
    s.update(i)
  s.print_scoreboard()

