a = 7
b = a
a = a + 1
print(b)

a = [1,2,3,4]
b = a
a.append(5)
print(b)

a = [3,1,2]
a.sort()
print(a[0])
a.append(4) #to add to list
print(a[3])
four = a.pop() #to remove from a list
print(four)

b = {"first":1, "second":2, "third":3}
b["first"] #gives us 1
b["fourth"] = 4 #to append a key to a dict
b.get("second", 0) #gives us 2, or 0 if key doesnt exist
del b['second'] #deletes this entry

c = set([1,2,3,4,5,5,5,5,6,7]) #sets only return unique values
print(c)

result = []
for i in range(10):
    result.append(i)

result = [i for i in range(10)] #list comprehension

result[3] #will return the 4th element
result[:3] #will return everything before the 4th element
result[3:] #will return everything from the 4th element on
result[3:7] #will return everything 4th to 7th but not including 7th
result[2::3] #will return everything from 2 by 3's
result[::-1] #will start backwards from the end

for a in [1,2,3]:
    print(a)   #do something for each element in a list

for a in range(len([1,2,3])):   #will do something to the indexes of the list
    print([1,2,3][a])  #will return the same as above

def add_one(x):
    return x + 1

answer = list(map(add_one, result)) #to use def function on all elements of the list 

