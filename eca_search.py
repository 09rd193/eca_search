# coding: utf-8
import csv

def onestep(line):
  newline = ''
  for i in range(len(line)):
    if len(line) == 1:
      return '10'
    x, z = '0', '0'
    if i == 0:
      x, z = '0', line[i + 1]
      if line[i] == '1':
        newline = '1' + newline
    elif i == len(line) - 1:
      x, z = line[i - 1], '0'
    else:
      x, z = line[i - 1], line[i + 1]
    newline += '0' if x == z else '1'
  return newline

def serch(target):
  item, tmp = '1', ''
  integer = int(item, 2)
  while True:
    if target == integer:
      break
    elif target < integer:
      item = tmp
      break
    else:
      tmp = item
    item = onestep(item)
    integer = int(item, 2)
  return item

def main():
  # targetよりも小さい値をECA上から探す
  target = 1234567890
  while 0 < target:
    result = serch(target)
    print('''rest: %d = %s - %s''' % (target - int(result, 2), target, int(result, 2)))
    target = target - int(result, 2)

if __name__ == '__main__':
  main()