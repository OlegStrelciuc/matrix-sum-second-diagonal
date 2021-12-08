matrix = [
    [1,2,4],
    [4,5,6],
    [7,8,9]
]


#ssd = matrix[0][2] + matrix[1][1] + matrix[2][0]
ssd = 0
for si in range(3):
    ssd = ssd + matrix[si][-1-si]

print("sum of secondary diagonal:", ssd)



smd = 0
for di in range(3):
    smd = smd + matrix[di][di]

print("sum of main diagonal:", smd)

for ri in range(3):
    row = matrix[ri]

    for ci in range(3):
        col = row[ci]
        print(ri, ci, ">", col)
