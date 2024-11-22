import random

population_size = 1000000
votes = [0] * population_size

for i in range(population_size):
  v = random.random()
  if v < 0.35:
    votes[i] = 1
  elif v < 0.75:
    votes[i] = -1
  else:
    votes[i] = 0

num_trials = 200
sample_size = 500

negative_majority_occurences = 0
for i in range(num_trials):
  random.shuffle(votes) # Might be an overkill or inefficient way to do the sampling without replacement, but it works for the experiment
  samples = [0] * sample_size
  for j in range(sample_size):
    samples[j] = votes[
        j]  # We can sample by taking first j votes from shuffled array
  if (samples.count(-1) > samples.count(0)
      and samples.count(-1) > samples.count(1)):
    negative_majority_occurences += 1
print(
    f"Probability -1 Majority: {negative_majority_occurences / num_trials}")
