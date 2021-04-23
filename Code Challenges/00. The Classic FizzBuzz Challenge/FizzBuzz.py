def FizzBuzz():
  for _ in range(1, 101):
    if _ % 5 == 0:
      if _ % 3 == 0:
        print('FizzBuzz')
      else:
        print('Buzz')
    elif _ % 3 == 0:
      print('Fizz')
    else:
      print(_)
