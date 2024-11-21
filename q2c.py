import random

t = 16 * 10**4

origin_crossings_per_run = []

for run in range(50):
  old_old_s = 0
  old_s = 0
  s = 0

  origin_crossings = 0
  for i in range(t):
    old_old_s = old_s
    old_s = s
    p = random.random()  # Random float between 0 and 1
    if p > 0.5:
      s += 1
      if old_old_s == -1 and old_s == 0:
        origin_crossings += 1
    else:
      s -= 1
      if old_old_s == 1 and old_s == 0:
        origin_crossings += 1
  origin_crossings_per_run.append(origin_crossings)

avg_crossings = sum(origin_crossings_per_run) / len(origin_crossings_per_run)
print(f"avg crossings of origin: {origin_crossings}")
