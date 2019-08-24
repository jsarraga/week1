from collections import Counter

def count_words(filename):
    with open(filename, 'r') as f:
        words = f.read().lower()
        word_list = words.split()
        allwords = [i for i in word_list if i.isalpha()]  #isalpha still counts punctuations
        dict_count = Counter(word_list)
        return dict_count
        

mydict = count_words('test.txt')
sorted_dict = mydict.keys()
for key, value in 

print(sorted_dict)