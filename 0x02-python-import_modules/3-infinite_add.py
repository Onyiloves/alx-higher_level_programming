#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

number = 0
length = len(argv)
for z in range(1, length):
    number += int(argv[z])
print('{}'.format(number))
