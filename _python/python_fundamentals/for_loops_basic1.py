# 1. Print all integers from 0 to 150.
for i in range(1, 151):
    print (i)

# 2. Print all the multiples of 5 from 5 to 1,000
for i in range(1, 1000): 
    if (i) % 5 == 0: 
        print (i) 

# # 3. Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 100):
    if (i) % 5:
        print("Coding")
    if (i) % 10:
        print ("Coding Dojo")

# 4. Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(1, 500000, 2):
    sum = sum + (i)
    print(sum) 

# 5 Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, -1, -4):
    print(i)
count = 2018
while count > -1:
    print("count")
    count = count -4



# 6. Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

numArr=[]

for i in range(lowNum, highNum+1):
    if i%mult == 0:
        numArr.append(i)

print(numArr)

    