class name:
  def main():
    name = input("What is your name?: ")
    for i in name:
        if i.isdigit():
            raise ValueError("The name must not contain numbers!") 
  
  
class calculator:
  def main2():
    try:
      a = int(input('A: '))
      sign = input('Sign: ')
      b = int(input('B: '))
      if sign == '/' and b == 0:
        raise ZeroDivisionError
      if sign != '+' and sign != '-' and sign!='*' and sign!='/':
        raise Warning
      elif sign == '+':
        print(f"{a} + {b} = {a+b}")
      elif sign == '-':
        print(f"{a} - {b} = {a-b}")
      elif sign == '*':
        print(f"{a} * {b} = {a*b}")
      elif sign == '*':
        print(f"{a} / {b} = {a/b}")
    except ValueError:
      print('You need to input digits!')
    except ZeroDivisionError:
      print('Go to school')
    except Warning:
      print('Unknown sign')
    except:
      print('Error!')

obj1 = name()
obj2 = calculator()