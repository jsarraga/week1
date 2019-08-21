with open('article.txt', 'r') as f:
    words = f.read()
    word_list = words.split()
    most_occur = 0
    i = word_list[0]
    for word in word_list:
        if word_list.count(word) > most_occur:
            most_occur = word_list.count(word)
            i = word         
    print(i, most_occur) 