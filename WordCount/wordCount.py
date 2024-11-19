from functools import reduce
from collections import defaultdict

def mapper(text):
    # Split the text into individual wors and return a list of (word, 1) tuples
    return [(word, 1) for word in text.split()]

def reducer(word_counts, pair):
    # Increment the count of the word in the word_counts dictionary
    word, count = pair
    word_counts[word] += count
    return word_counts

with open("files/Words.txt", "r") as f:
    input_texts1 = f.read()
    input_texts = input_texts1.split()

# Step 1: Map - apply the mapper function to each input text
mapped_data = list(map(mapper, input_texts))

# Words_Map.txt 
with open("Words_Map.txt", "w") as f:
    for line in mapped_data:
        for word, count in line:
            f.write(f"{word},{count}\n")

# Step 2: Flatten the mapped data into a single list of (word, 1) tuples
flattened_data = [pair for sublist in mapped_data for pair in sublist]

# Words_Shuffle.txt 
with open("Words_Shuffle.txt", "w") as f:
    for word, count in flattened_data:
        f.write(f"{word},{count}\n")

# Step 3: Reduce - apply the reducer function to the list of tuplrs to get the word counts
word_counts = reduce(reducer, flattened_data, defaultdict(int))

# Words_Reduce.txt
with open("Words_Reduce.txt", "w") as f:
    for word, count in word_counts.items():
        f.write(f"{word},{count}\n")

# Step 4: Display the word counts
print(dict(word_counts))
