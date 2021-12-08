import os

def main():
  i = 0
  prev = None
  with open("day1_1_input.txt", "r") as file:
    for line in file:
      curr = int(line)
      if not prev == None and curr > prev:
        i = i + 1
      prev = curr

  print(f"Answer: {i}")

if __name__ == "__main__":
  main()
