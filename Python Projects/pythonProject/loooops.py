#loops
#FORLOOPS
ln=[1,23,45,67,8,4,42,11,3]
sum=0
for val in ln:
 sum+=val
print("the sum is", sum)

#print all the tables
for i in range(1, 11):
    table_row = ""
    for j in range(1, 11):
        table_row += str(i * j) + "\t"
    print(table_row)
