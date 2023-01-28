@@ -5,13 +5,21 @@ def __init__(self, name):
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
@@ -26,7 +34,7 @@ def sleep(self):
	def say_hello(self):
		print('Hello!')
	def live(self):
		live_cube = randint(1,4)
		live_cube = randint(1,6)
		if live_cube == 1:
			self.study()
		elif live_cube == 2:
@@ -35,7 +43,9 @@ def live(self):
			self.sleep()
		elif live_cube == 4:
			self.say_hello()
		elif live_cube == 5:
    elif live_cube == 5:
			self.food()
		elif live_cube == 6:
			self.work()
		self.final()
	def final(self):
@@ -61,6 +71,7 @@ def feding(self):
    self.hungry -= 30
    self.thirsty += 10
    self.play -= 10
    self.food -= 1
    print('Time to eat!')
  def drinking(self):
    self.thirsty -= 30
@@ -92,7 +103,7 @@ def final(self):
      self.alive = False

print('Rose\'s life')
obj1 = Student('Bob')
obj1 = Student('Rose')
for i in range(365):
	if obj1.alive == False:
		break