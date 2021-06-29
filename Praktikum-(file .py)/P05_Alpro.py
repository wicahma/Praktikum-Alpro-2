#Bubble Sort Ascending
def bubble2(A):
    tukar=True
    while tukar:
        tukar=False
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                tukar=True
    return A

A=[1,4,3,2,78,5,4,9,8,21]
bubble2(A)

#1. Pengurutan descending
#Bubble Sort Ascending
def bsort_asc(data):
    tukar=True
    while tukar:
        tukar=False
        for ank1 in range(len(data)-1):
            ank2=ank1+1
            if data[ank1]>data[ank2]:
                data[ank1],data[ank2]=data[ank2],data[ank1]
                tukar=True
    print('data anda setelah diurutkan: ',data)
    return data


data=[]
#Fungsi Input data
def inp_data():
    while True:
        inp=input('Masukkan data: ')
        if inp=='00':
            break
        else:
            data.append(float(inp))
    return inp

#Fungsi Perulangan
loop='y'
while loop=='y':
    print('''==Bubble Sort Ascending==
tekan 00 untuk selesai\n''')
    inp_data()
    bsort_asc(data)
    del data[0:len(data)+1]
    print('''\ntekan sembarang untuk selesai, y untuk lanjut
Apakah anda ingin mengurutkan lagi?''')
    loop=input('==>')

print('Program selesai...')

#Bubble Sort Descending
def bsort_asc(data):
    tukar=True
    while tukar:
        tukar=False
        for ank1 in range(len(data)-1):
            ank2=ank1+1
            if data[ank1]<data[ank2]:
                data[ank1],data[ank2]=data[ank2],data[ank1]
                tukar=True
    print('data anda setelah diurutkan: ',data)
    return data

data=[]
#Fungsi Input data
def inp_data():
    while True:
        inp=input('Masukkan data: ')
        if inp=='00':
            break
        else:
            data.append(float(inp))
    return inp

#Fungsi Perulangan
loop='y'
while loop=='y':
    print('''==Bubble Sort Ascending==
tekan 00 untuk selesai\n''')
    inp_data()
    bsort_asc(data)
    del data[0:len(data)+1]
    print('''\ntekan sembarang untuk selesai, y untuk lanjut
Apakah anda ingin mengurutkan lagi?''')
    loop=input('==>')

print('Program selesai...')


#2. Dengan modifikasi penjelasan
# Bubble Sort Ascending dengan penjelasan lebih lengkap
def bsort_asc(data):
    tukar=True
    while tukar:
        tukar=False
        for ank1 in range(len(data)-1):
            ank2=ank1+1
            if data[ank1]>data[ank2]:
                data[ank1],data[ank2]=data[ank2],data[ank1]
                print('\ntukar',data[ank1],'dengan',data[ank2])
                print('data setelah ditukar: ',data)
                tukar=True
    return data


data=[]
#Fungsi Input data
def inp_data():
    while True:
        inp=input('Masukkan data: ')
        if inp=='00':
            break
        else:
            data.append(float(inp))


#Fungsi Perulangan
loop='y'
while loop=='y':
    print('''==Bubble Sort Ascending==
tekan 00 untuk selesai\n''')
    inp_data()
    bsort_asc(data)
    print('\ndata akhir anda:',data)
    del data[0:len(data)+1]
    print('''\ntekan sembarang untuk selesai, y untuk lanjut
Apakah anda ingin mengurutkan lagi?''')
    loop=input('==>')

print('Program selesai...')