coins = [int(x) for x in input()]
boxes = [0 for _ in range(5)]

for i in range(len(coins)):
    boxes[i % 5] += coins[i]

print(boxes.index(max(boxes)) + 1)
