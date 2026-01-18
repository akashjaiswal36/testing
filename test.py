import datetime
duplicate = {}
listt = [1,2,3,4,5,6,4,1,4,4,3,3,4,6,7,8,9,9,9,8,7,7,7,7,7,8,8,7,7,6,5,4,4,4,6,6,66666]
for i in listt:
    duplicate[i] = duplicate.get(i, 0) + 1

print(duplicate)

max_value = max(duplicate.values())
print(max_value)
max_key =  [k for k, v in duplicate.items() if v == max_value]

date = datetime.datetime.now()

print(f"{max_key} : {max_value} ==> {date}") 
 

