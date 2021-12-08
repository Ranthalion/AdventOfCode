import os

def main():
  x = 0
  y = 0
  aim = 0

  with open("day2_input.txt", "r") as file:
    for line in file:
      command, amount = line.split()
      amount = int(amount)
      if command == 'forward':
        x += amount
        y += (amount * aim)
      elif command == 'up':
        aim -= amount
      elif command == 'down':
        aim += amount
      else:
        print(f'Invalid command {line}')
        exit()

  print(f"Answer: ({x}, {y}) =  {x * y}")

if __name__ == "__main__":
  main()
