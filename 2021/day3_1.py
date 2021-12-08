import os

def main():
  num_bits = 12
  val = [0] * num_bits
  gamma = ''
  epsilon = ''

  with open("day3_input.txt", "r") as file:
    for line in file:
      for x in range(num_bits):
        if line[x] == '0':
          val[x] -= 1
        else:
          val[x] += 1

  for x in val:
    if x > 0:
      gamma += '1'
      epsilon += '0'
    else:
      gamma += '0'
      epsilon += '1'

  answer = int(gamma, 2) * int(epsilon,2)
  print(f'gamma: {gamma}\tepsilon: {epsilon}\tanswer: {answer}')

if __name__ == "__main__":
  main()
