n = int(input('insert the number of student: '))
name_score={}
for i in range(n):
    Name, *Scores = input('insert name and scores: ').split()
    Scores = list(map(float,Scores))
    name_score[Name] = Scores

query_name = input('insert the one who you wants the average: ')
average= sum(name_score[query_name])/3
print("%.2f" % average)