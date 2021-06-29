#NumPy
import numpy as np
matr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matr)

matr1=[[a for y in range(10)] for x in range(4)]
matr1

matr2=np.zeros((2,15))
print(matr2)

np.random.rand(2,4)

matr3=np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print('The choosen One, is you:',matr3[1][1])

ma1=[[2,5,3],
     [1,7,2],
     [3,5,0]]

ma2=[[6,4,2],
     [7,5,9],
     [0,0,1]]

for x in range(0,len(ma1)):
    for y in range(0,len(ma1[0])):
        print(ma1[x][y] + ma2[x][y],end=' ')
    print()

ma1=[[2,5,3],
     [1,7,2],
     [3,5,0]]

ma2=[[6,4,2],
     [7,5,9],
     [0,0,1]]

ma3=[]
#perkalian
for x in range(0,len(ma1)):
    row=[]
    for y in range (0,len(ma1)):
        total=0
        for z in range(0,len(ma1)):
            total=total+(ma1[x][z]*ma2[z][y])
        row.append(total)
    ma3.append(row)

#Display
for x in range(0,len(ma3)):
    for y in range(0,len(ma3[0])):
        print(ma3[x][y],end=' ')
    print()


matr4=np.array([[6,4,2],
                [7,5,9],
                [0,0,1]])
print('Sebelum urut: \n',matr4,'\nSesudah urut :\n',matr4.T)

matr5=np.array([[9,2,5],
       [1,7,1],
       [3,5,-6]])

print('Matriks\n',matr5,'\nNilai max\n',np.max(matr5),'\nNilai min\n',np.min(matr5),'\nStandar Dev\n', round(np.std(matr5),2),'\nRata Rata\n',np.mean(matr5),'\nVarian/Ragam\n',round(np.var(matr5),2))

#Tugas
#Run terlebih dahulu cell matriks ini, agar command yang ada dibawahnya dapat di proses
mat=[[5,0,8],
     [2,6,7],
     [1,3,4]]

#no 1
print(mat[1][1])

#no 2
print(mat[1][2])

#no 3
print('Cara 1=',mat[2])

#atau

for a in range(2,len(mat)):
    print('Cara 2',end='= ')
    for b in range(len(mat)):
        print(mat[a][b],end=' ')
    print()

#no 4
print('Cara 1=',[baris[0] for baris in mat])

#atau

print('Cara 2=',end=' ')
for a in range(len(mat)):
    for b in range(len(mat)-2):
        print(mat[a][b],end=' ')



