class literature:
  def __init__ (self, title):
    self.author = 'None' 
    self.title = title
    self.genre = 'None'
  def read(self):
    print(self.title+'is being read')

class Book(literature):
  def __init__ (self, title):
    super().__init__(title)
    self.pages = 0
  def read(self):
    super().read( )
    print('I like to read', self.title)
  def write(self) :
    print('I write fanfic of', self.title)

class Magazine(literature):
  def __init__ (self, title):
    super().__init__(title)
    self.pictures = 0
  def read(self):
    super().read( )
    print('I like to read', self.title)
  def picture(self) :
    print('I am looking at pictures of', self.title)

book1 = Book('Harry Potter') 
book1.read()
book1.write()
magazine1 = Magazine('The Daily Gazetteer') 
magazine1.read()
magazine1.picture()