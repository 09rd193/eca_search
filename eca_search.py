# coding: utf-8
import csv

def onestep(line):
  newline = ''
  for i in range(len(line)):
    x, z = '0', '0'
    if i == 0:
        x, z = '0', line[i + 1]
        newline = '1' + newline if line[i] == '1' else newline
    elif i == len(line) - 1:
        x, z = line[i - 1], '0'
    else:
        x, z = line[i - 1], line[i + 1]
    newline += '0' if x == z else '1'
  return newline

def serch(target):
  item, tmp = '01', ''
  integer = int(item, 2)
  while True:
    if target < integer:
      item = tmp
      break
    elif target == integer:
      break
    else:
      tmp = item
    item = onestep(item)
    integer = int(item, 2)
  return item

def main():
  # targetよりも小さい値をECA上から探す
  target = 544
  result = serch(target)
  print(result)
  print(int(result, 2))

if __name__ == '__main__':
  main()