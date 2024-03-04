def count_word_occurrences(filename):
 
  word_counts = {}
  try:
    with open(filename, 'r') as f:
      for line in f:
        words = line.lower().split()
        for word in words:
          if word in word_counts:
            word_counts[word] += 1
          else:
            word_counts[word] = 1
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  return word_counts
 
filename = "testing.txt"
word_counts = count_word_occurrences(filename)
 
if word_counts:
  for word, count in word_counts.items():
    print(f"{word}: {count}")
else:
  print("No words found in the file.")