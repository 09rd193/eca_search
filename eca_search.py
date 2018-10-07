# coding: utf-8
import math

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

def inititem(target):
  digit = int(math.log2(target))
  intitem = 2 ** digit
  stritem = format(intitem, 'b')
  _stritem = '1'
  while len(_stritem) <= len(stritem):
    _stritem = _stritem + '0' * len(_stritem)
  stritem = _stritem[:int(-len(_stritem) / 2)]
  return stritem

def serch(target):
  item, tmp = inititem(target), ''
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

def gethexdata(datapath):
  data = ''
  with open(datapath, mode='rb') as f:
    data = f.read().hex()
  return data

def main():
  # targetよりも小さい値をECA上から探す
  hexdata = gethexdata('./lenna.png')
  target = int(hexdata, 16)
  while 0 < target:
    result = serch(target)
    print(len(result), 'step')
    target = target - int(result, 2)
if __name__ == '__main__':
  main()