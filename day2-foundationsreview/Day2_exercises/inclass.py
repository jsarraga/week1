a = 7
b = a
a = a + 1
# print(b)

a = [1,2,3,4]
b = a
a.append(5)
print(b)

a = [3,1,2]
a.sort()
print(a[0])
a.append(4)
print(a[3])
four = a.pop()
print(four)

b = {"first":1, "second":2, "third":3}
b["first"] # gives us 1
b["fourth"] = 4
b.get("second", 0) # gives us 2, or 0 if key doesn't exist
del b['second'] #deletes this entry

c = set([1,2,3,4,5,5,5,5,6,7])
print(c)

result = []
for i in range(10):
    result.append(i)

result = [i for i in range(10)]

result[:3]
result[3:]
result[3:7]
result[2::3]
result[::-1]

for a in [1,2,3]:
    print(a)

for a in range(len([1,2,3])):
    print([1,2,3][a])

def add_one(x):
    return x + 1

answer = list(map(add_one, result))
