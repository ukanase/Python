for i in range(5, 0, -1):
    print(i)

# for element in [1, 2, 3]:
#     print(element)
# for element in (1, 2, 3):
#     print(element)
# for key in {'one':1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)
# for i, char in enumerate("abcde"):
#     print(f"{i} {char}")


# # for line in open("myfile.txt"):
# #     print(line, end='')
    
# # Generator expressions
# sum(i*i for i in range(10))                 # sum of squares
# 285

# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# sum(x*y for x,y in zip(xvec, yvec))         # dot product
# 260
# page  = []
# unique_words = set(word for line in page  for word in line.split())
# graduates = []
# # valedictorian = max((student.gpa, student.name) for student in graduates)

# data = 'golf'
# list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']