num_rows = int(input('Enter the number of rows\n'))

for i in range(1, num_rows + 1):
    stars = 2*i - 1
    spaces = 10 - i
    print(' ' * spaces + '*' * stars)

for i in range(num_rows - 1, 0, -1):
    stars = 2*i - 1
    spaces = 10 - i
    print(' ' * spaces + '*' * stars)
