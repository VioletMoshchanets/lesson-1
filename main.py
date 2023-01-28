from random import randint
class Student:
	def __init__(self, name):
		self.name = name
		self.gladness = 0
		self.progress = 0
		self.money = 0
    self.food = 0
		self.alive = True
	def education(self, Pet):
		print(self.name, 'loking for', Pet.title)
	def work(self):
		self.money += 50
		self.progress -= 5
		print('Work time')
  def shop(self):
    if self.money >= 10
		  self.money -= 10
		  self.food += 1
		  print('Time buy food for pet')
    if self.money < 10
		  print('You have not enought money')
	def study(self):
		self.progress += 20
		self.gladness -= 10
		print('Study time')
	def chill(self):
		self.gladness += 35
		self.progress -= 8
		print('Chill time')
	def sleep(self):
		self.gladness += 4
		print('Sleep time')
	def say_hello(self):
		print('Hello!')
	def live(self):
		live_cube = randint(1,6)
		if live_cube == 1:
			self.study()
		elif live_cube == 2:
			self.chill()
		elif live_cube == 3:
			self.sleep()
		elif live_cube == 4:
			self.say_hello()
    elif live_cube == 5:
			self.food()
		elif live_cube == 6:
			self.work()
		self.final()
	def final(self):
		if self.progress == 100:
			print('Amazing! You graduated!')
			self.alive = False
		elif self.progress < -20:
			print('Too bad... You are stupid')
			self.alive = False
		elif self.gladness < -20:
			print('Depression :(')
			self.alive = False

class Pet:
  def __init__(self, title):
    self.hungry = 40
    self.title = title
    self.thirsty = 40
    self.play = 0
  def loking_for(self, Student):
    print(Student.name, 'is loking for pet')
  def feding(self):
    self.hungry -= 30
    self.thirsty += 10
    self.play -= 10
    self.food -= 1
    print('Time to eat!')
  def drinking(self):
    self.thirsty -= 30
    self.play -= 10
    print('Time to drink!')
  def playing(self):
    self.hungry += 30
    self.thirsty += 30
    self.play += 30
    print('Time to play!')
  def live(self):
    live_cube = randint(1,3)
    if live_cube == 1:
      self.hungry()
    elif live_cube == 2:
      self.thirsty()
    elif live_cube == 3:
      self.play()
    self.final()
  def final(self):
    if self.play == 100:
      print('Amazing! Pet happy!')
      self.alive = False
    elif self.thirsty == 100:
      print('Too bad... Pet die...')
      self.alive = False
    elif self.hungry == 100:
      print('Too bad... Pet die...')
      self.alive = False

print('Rose\'s life')
obj1 = Student('Rose')
for i in range(365):
	if obj1.alive == False:
		break
	obj1.live()