def happy(func):
  def wrapper():
    print('I am happy')
    func()
  return wrapper

def sad(func):
  def wrapper():
    print('I am sad')
    func()
  return wrapper

def angry(func):
  def wrapper():
    print('I am angry')
    func()
  return wrapper

def scary(func):
  def wrapper():
    print('I am scary')
    func()
  return wrapper

def embarrassed(func):
  def wrapper():
    print('I am embarrassed')
    func()
  return wrapper

def amazed(func):
  def wrapper():
    print('I am amazed')
    func()
  return wrapper

def suprised(func):
  def wrapper():
    print('I am surprised')
    func()
  return wrapper

def good(func):
  def wrapper():
    print('I am good')
    func()
  return wrapper

def disappointed(func):
  def wrapper():
    print('I am disappointed')
    func()
  return wrapper

def disgust(func):
  def wrapper():
    print('I feel disgust')
    func()
  return wrapper

@happy
@sad
@angry
@scary
@embarrassed
@amazed
@suprised
@good
@disappointed
@disgust
def human():
  print('I am human')
human()