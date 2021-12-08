import os

def main():
  i = 0
  line_num = 0
  vals = [0, 0, 0, 0]
  with open("day1_1_input.txt", "r") as file:
    for line in file:
      idx = line_num%4
      vals[idx] = int(line)
      line_num = line_num + 1
      if line_num < 4:
        continue

      incoming = vals[idx]
      outgoing = vals[0 if idx == 3 else idx+1]
      if (incoming > outgoing):
        i = i + 1

  print(f"Answer: {i}")

if __name__ == "__main__":
  main()
