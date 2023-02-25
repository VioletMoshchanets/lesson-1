class character:
  def __init__ (self, title):
    self.superpower = 'None' 
    self.name = title
  def fight(self):
    print(self.name+' is fighting')

class Hero(character):
  def __init__ (self, title):
    super().__init__(title)
    self.lives_saved = 0
  def fight(self):
    super().fight( )
    print('Yes, babe, it`s me', self.name)
  def greetings(self) :
    print('Everything will be fine because I`m here', self.name)
  def win(self) :
    print('I told you that I would win')

class Villian(character):
  def __init__ (self, title):
    super().__init__(title)
    self.lives_killed = 0
  def fight(self):
    super().fight( )
    print('I`m not your babe because I ', self.name)
  def shut_up(self) :
    print('Shut up stupid hero! I will win because I great', self.name)
  def lose(self) :
    print('You didn`t say that and next time I will defeat you!')

good = Hero('Sweet hero')
bad = Villian('Grumbler') 
good.greetings()
bad.shut_up()
good.fight()
bad.fight()
good.win()
bad.lose()