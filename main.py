class animal:
  def __init__(self, name):
    self.name = name
    self.age = 0
  def live(self):
    print(self.name,' is living')

class dog (animal):
  def __init__(self, name):
    super().__init__(name)
    self.stick = 0
  def live(self):
    super().live()
    print('Day of',self.name,'life')
  def looking_for_a_stick(self):
    print('Dog is looking for a stick')

class cat (animal):
  def __init__(self, name):
    super().__init__(name)
    self.mouse = 0
  def live(self):
    super().live()
    print('Day of',self.name,'life')
  def looking_for_a_mouse(self):
    print('Cat is looking for a mouse')

class hamster (animal):
  def __init__(self, name):
    super().__init__(name)
    self.seed = 0
  def live(self):
    super().live()
    print('Day of',self.name,'life')
  def looking_for_a_seed(self):
    print('Hamster is looking for a seed')

obj1 = dog('Mily')
obj1.live()
obj1.looking_for_a_stick()
obj2 = cat('Ash')
obj2.live()
obj2.looking_for_a_mouse()
obj3 = hamster ('Lily')
obj3.live()
obj3.looking_for_a_seed()