import random

# Simulate tossing a coin 200 times
tosses = [random.choice(['heads', 'tails']) for _ in range(200)]

# Calculate the proportion of heads
num_heads = tosses.count('heads')
proportion_heads = num_heads / len(tosses)

print(f"Number of heads: {num_heads}")
print(f"Proportion of heads: {proportion_heads:.2f}")