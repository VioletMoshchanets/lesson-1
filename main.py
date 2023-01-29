class Human:
  def __init__(self, name):
    self.name = name
    self.age = 0
    self.poor_eyesight = 0
  def live(self):
    print(self.name,' is living')
  def school(self):
    print(self.name,' is at school')

class Teacher (Human):
  def __init__(self, name):
    super().__init__(name)
    self.lessons_per_day = 0
  def live(self):
    super().live()
    print('Day of',self.name,'life')
  def drink_coffee(self):
    print('Teacher drinking coffee')
  def give_bad_marks(self):
    print('Teacher give bad marks for students')

class Student (Human):
  def __init__(self, name):
    super().__init__(name)
    self.finished_pens = 0
  def live(self):
    super().live()
    print('Day of',self.name,'life')
  def run_at_recess(self):
    print('Student runing at recess')
  def get_bad_mark(self):
    print('Student get bad mark')

obj1 = Teacher('Maria Ivanovna')
obj1.live()
obj1.school()
obj1.drink_coffee()
obj1.give_bad_marks()
obj2 = Student('Vova')
obj2.live()
obj2.school()
obj2.run_at_recess()
obj2.get_bad_mark()