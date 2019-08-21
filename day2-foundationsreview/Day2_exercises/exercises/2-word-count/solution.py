from collections import Counter 


def word_stats(x, n):
    f = open(x, "r")
    words = f.read().lower()
    word_list = words.split()
    x = Counter(word_list).most_common(n)
    print(x)

word_stats("article.txt", 10)