# names = []
# genders = []
# scores = []

# with open("yob1995.txt") as f:
#     lines = f.readlines()
#     for line in lines:
#         name, gender, score = line.strip().split(',')
#         names.append(name)
#         genders.append(gender)
#         scores.append(score)

# data = [(a, b, c) for a, b, c in zip(names, genders, scores)]
# females = [item for item in data if item[1]=='F']
# print(sorted(females, key=lambda x:int(x[2]), reverse=True)[1])

f = open("yob1995.txt", 'r')
maxname = "none"
maxval = 0
max2name = "none"
max2val = 0
for line in f:
    (name,sex,count) = line.split(',')
    count = int(count)
    if sex == 'F':
        if count > maxval:
            max2name = maxname
            max2val = maxval
            maxval = count
            maxname = name
        elif count > max2val:
            max2name = name
            max2val = count
print(maxname, max2name)
print(maxval, max2val)