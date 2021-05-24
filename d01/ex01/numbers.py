# !/usr/bin/python3

TARGET="numbers.txt"

def read_target():
  f = open(TARGET, 'r')
  while (True):
      line = f.readline()
      if not line: break
      print_line(line)
  f.close()
  print_line(line)

def print_line(line: str):
  nodes = line.split(",")
  for node in nodes:
    print(node);

if __name__ == '__main__':
  read_target()
