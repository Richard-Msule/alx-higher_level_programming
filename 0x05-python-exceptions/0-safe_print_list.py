#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
  printed = 0
  try:
    while x > 0:
      print(my_list[printed], end=' ')
      printed += 1
      x -= 1
  except IndexError:
    pass
  print()
  return printed

