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