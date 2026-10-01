numbers = [3, 7, 2, 9, 7, 10, 3, 8]

# Count occurrences of each value
counts = {}
for num in numbers:
    counts[num] = counts.get(num, 0) + 1
print(sorted(counts))

# Find the value(s) with the highest count
max_count = max(counts.values())
print(counts.items())
modes = [num for num, count in counts.items() if count == max_count]


print("Mode(s):", modes)
print(modes[0], modes[1])