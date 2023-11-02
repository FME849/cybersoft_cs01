import method
#input
toan:float = float(input("Please input math score: "))
ly:float = float(input("Please input physic score: "))
hoa:float = float(input("Please input chemistry score: "))

#output
average_score:float = 0
classification:str = ''

average_score = method.calculate_average_score(toan, ly, hoa)
classification = method.classify(average_score)

print(average_score)
print(classification)