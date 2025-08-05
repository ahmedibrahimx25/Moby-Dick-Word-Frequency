
"""
Word Frequency in Classic Novels: Moby Dick

This script downloads Moby Dick from Project Gutenberg, cleans and analyzes the text,
and visualizes the most frequent words.
"""

import requests
import re
import nltk
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Download the novel
url = 'https://www.gutenberg.org/files/2701/2701-0.txt'
response = requests.get(url)
response.encoding = 'utf-8'
text = response.text

# 2. Extract main content
def extract_main_text(text):
    start_marker = 'CHAPTER 1. Loomings.'
    end_marker = 'End of the Project Gutenberg EBook of Moby Dick; or The Whale, by Herman Melville'
    start = text.find(start_marker)
    end = text.find(end_marker)
    if start == -1 or end == -1:
        return text
    return text[start:end]

main_text = extract_main_text(text)

# 3. Clean and tokenize
def clean_and_tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return words

words = clean_and_tokenize(main_text)

# 4. Remove stopwords
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]

# 5. Count word frequencies
word_counts = Counter(filtered_words)
top_100 = word_counts.most_common(100)

# 6. Save and visualize
# Save to CSV
top_100_df = pd.DataFrame(top_100, columns=['word', 'count'])
top_100_df.to_csv('moby_dick_top100_words.csv', index=False)

# Plot top 30 for readability
plt.figure(figsize=(10, 12))
sns.set_style('whitegrid')
sns.barplot(data=top_100_df.head(30), y='word', x='count', palette='Blues_d')
plt.title('Top 30 Most Frequent Words in Moby Dick')
plt.xlabel('Count')
plt.ylabel('Word')
plt.tight_layout()
plt.savefig('moby_dick_top30_words.png', dpi=300)
plt.show()
