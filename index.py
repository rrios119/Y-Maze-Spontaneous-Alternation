import pandas as pd
from itertools import groupby

file = input('What is the name of your CSV file? Ex: ymaze.csv ' + '\n')

df = pd.read_csv(file, usecols = ['In top', 'In left', 'In right'])

top_list = df['In top'].tolist()
left_list = df['In left'].tolist()
right_list = df['In right'].tolist()

A = []
B = []
C = []

for i in range(len(top_list)):
    if (top_list[i] == 1):
        A.append('A')
    else:
        A.append('X')

for i in range(len(left_list)):
    if (left_list[i] == 1):
        B.append('B')
    else:
        B.append('X')

for i in range(len(right_list)):
    if (right_list[i] == 1):
        C.append('C')
    else:
        C.append('X')
        
ymaze_temp = [] #temporary list with duplicates
ymaze = [] #final list without duplicates

for i in range(len(A)): #joining the A's, B's and C's together
    if (A[i] == 'A'):
        ymaze_temp.append(A[i])
    elif (B[i] == 'B'):
        ymaze_temp.append(B[i])
    elif (C[i] == 'C'):
        ymaze_temp.append(C[i])

ymaze = [i[0] for i in groupby(ymaze_temp)]

limit = len(ymaze) - 2
temp_patterns = []
patterns = []

total_ABC = 0

verify = False

for i in range(len(ymaze)):
    if (i == limit):
        break
    temp_patterns.append(ymaze[i] + ymaze[i + 1] + ymaze[i + 2])
    temp = ""
    temp = temp.join(temp_patterns[i])
    for z in range(1):
        for x in range(len(temp) - 2):
            for y in range(1 ,len(temp)):
                if (temp[x] == temp[y]):
                    verify = False
                    break
                elif (temp[y - 1] == temp[z + 2]):
                    verify = False
                    break
                else:
                    verify = True
    if (verify == True):
        total_ABC = total_ABC + 1
        patterns.append(temp)

print('Unique Arm Entries: ' + str(total_ABC))
print(str(patterns) + '\n')

print('Total Arm Entries: ' + str(len(temp_patterns)))
print(str(temp_patterns) + '\n')

print('Individual Arm Entries: ' + str(len(ymaze)))
print(str(ymaze) + '\n')

outputTextFile = input('What would you like to name the output text file? Ex: output.txt' + '\n')

textfile = open(outputTextFile, 'w')

textfile.write("Unique Arm Entries: " + str(total_ABC) + '\n')   
textfile.write(str(patterns) + '\n')

textfile.write('\n' + 'Total Arm Entries: ' + str(len(temp_patterns)) + '\n')
textfile.write(str(temp_patterns) + '\n')

textfile.write('\n' + 'Individual Arm Entries: ' + str(len(ymaze)) + '\n')
textfile.write(str(ymaze) + '\n')