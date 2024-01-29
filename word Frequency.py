from collections import Counter
import string

# Read the text file
with open('python_website_data.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Remove punctuation and convert text to lowercase
translator = str.maketrans('', '', string.punctuation)
cleaned_content = content.translate(translator).lower()

# Split the text into words
words = cleaned_content.split()

# Calculate word frequencies using Counter
word_frequencies = Counter(words)

# Display word frequencies
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
