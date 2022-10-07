
"""
Practice 1
Name:楊薇蓉
Student Number:110403537
Course: 2022-CE1003-A
"""
score=[]
standard=[12,12,8,12]
correct=1
print("Please enter your Chinese score:",end=' ')
score.append(int(input()))
print("Please enter your English score:",end=' ')
score.append(int(input()))
print("Please enter your Math score:",end=' ')
score.append(int(input()))
print("Please enter your Science score:",end=' ')
score.append(int(input()))

for i in range(len(score)):
    if(score[i]<standard[i]):
        correct=0
        break
if(correct==0):
    print("Sorry, you can't enter NCU CSIE.")
else:
    print("Welcome to NCU CSIE!")