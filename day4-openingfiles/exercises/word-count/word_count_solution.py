from collections import Counter

def count_words(filename):
    with open(filename, 'r') as f:
        words = f.read().lower()
        word_list = words.split()
        allwords = [i for i in word_list if i.isalpha()]  #isalpha still counts punctuations
        dict_count = Counter(word_list)
        return dict_count
        

def most_common(word_counts, n):
        x = Counter(word_counts).most_common(n)
        print(x)

most_common(count_words('article.txt'), 10)

