def pencseq(ank,cari):
    sis=[]
    for i in range(len(ank)):
        if ank[i]==cari:
            sis.append(i+1)
    if len(sis)>0:
        print('data',cari,'sebanyak',len(sis),'ditemukan di posisi',sis)
    else:
        print('data tidak ditemukan')
    return sis

ank=[4,2,1,7,2,3,9,10,5,2,4,1,2,6,4,7,9,7,2,5,1,6]
cari=2
pencseq(ank,cari)

def pencbin(ank,cari):
    awal=1
    akhir=len(ank)+1
    ketemu=False
    while (awal<=akhir) and not ketemu:
        tengah=int((awal+akhir)/2)
        if cari==ank[tengah]:
            ketemu=True
            print('ank',cari,'ditemukan di posisi',tengah)
        elif(cari<ank[tengah]):
            akhir=tengah-1
        else:
            awal=tengah+1
    if ketemu==False:
        print('Angka tidak ditemukan')

ank=[1,2,2,3,4,4,4,5,5,6,6,6,7,8,9,9,9,10,11,11,17]
cari=3
pencbin(ank,cari)

#1. Seq search integer dengan Manual Input
def pencseq(ank,cari):
    sis=[]
    for i in range(len(ank)):
        if ank[i]==cari:
            sis.append(i+1)
    print('\nJumlah Iterasi:',i+1)
    if len(sis)>0:
        print('Data dicari:',cari,'\nJumlah angka %d:'%(cari),len(sis),'\nPosisi angka:',sis)
    else:
        print('Data tidak ditemukan')
    return sis

def dataank(ank):
    while True: 
        inp_data=input('Data:')
        if inp_data=='00':
            break
        else:
            ank.append(int(inp_data))

print('''==Pencarian Sequential
Memasukkan data dan kata kunci 
pencarian secara manual

tekan 00 untuk mengakhiri pemasukan data
tekan enter untuk lanjut
''')

ank=[]
dataank(ank)
print('List Data', ank)
cari=int(input('\nCari Angka:'))
pencseq(ank,cari)

#2. Seq search string dengan Manual Input
def pencseq(stri,cari):
    sis=[]
    for i in range(len(stri)):
        if stri[i]==cari:
            sis.append(i+1)
    print('\nJumlah Iterasi: ',i+1)
    if len(sis)>0:
        print('Data: ',cari,'\nJumlah %s: '%(cari),len(sis),'\nPosisi data: ',sis)
    else:
        print('Data tidak ditemukan')
    return sis


print('''==Pencarian Sequential
Memasukkan data dan kata kunci 
pencarian secara manual

tekan 00 untuk mengakhiri pemasukan data
tekan enter untuk lanjut
''')

stri=str(input('Masukkan data: '))
print('List Data', stri)
cari=input('\nCari data:')
pencseq(stri,cari)

#3. Bin search integer dengan Manual Input
def pencbin(ank,cari):
    awal=1
    akhir=len(ank)+1
    ketemu=False
    iter=0
    while (awal<=akhir) and not ketemu:
        iter+=1
        tengah=int((awal+akhir)/2)
        if cari==ank[tengah]:
            ketemu=True
            print('Angka',cari,'Ditemukan di posisi:',tengah)
        elif(cari<ank[tengah]):
            akhir=tengah-1
        else:
            awal=tengah+1
    if ketemu==False:
        print('Angka tidak ditemukan')
    print('Jumlah Iterasi:',iter)
    
def dataank(ank):
    while True: 
        inp_data=input('Data:')
        if inp_data=='00':
            break
        else:
            ank.append(int(inp_data))
    ank.sort()

print('''==Pencarian Binary
Memasukkan data dan kata kunci 
pencarian secara manual

tekan 00 untuk mengakhiri pemasukan data
tekan enter untuk lanjut...
''')

ank=[]
dataank(ank)
print('List Data', ank)
cari=int(input('\nCari Angka:'))
pencbin(ank,cari)

#4. Bin search string
def pencbin(hur,cari):
    awal=1
    akhir=len(hur)+1
    ketemu=False
    iter=0
    while (awal<=akhir) and not ketemu:
        iter+=1
        tengah=int((awal+akhir)/2)
        if cari==hur[tengah]:
            ketemu=True
            print('Huruf',cari,'Ditemukan di posisi:',tengah)
        elif(cari<hur[tengah]):
            akhir=tengah-1
        else:
            awal=tengah+1
    if ketemu==False:
        print('Huruf tidak ditemukan')
    print('Jumlah Iterasi:',iter)
    
inp_hur="samlekom mamank"
print('Data awal:',inp_hur)
hur=''.join(sorted(inp_hur))
print('Data urut:',hur)
cari='a'
pencbin(hur,cari)

#5. Sequential NIM Search
def pencseq(nim,cari):
    sis=[]
    for i in range(len(nim)):
        if nim[i]==cari:
            sis.append(i+1)
    print('\nJumlah Iterasi:',i+1)
    if len(sis)>0:
        print('Data yang dicari:',cari,'\nJumlah angka %d:'%(cari),len(sis),'\nPosisi angka:',sis)
    else:
        print('Data tidak ditemukan')
    return sis

nim=[2,0,0,0,0,1,6,0,1,5]
print('List Data', nim)
cari=0
pencseq(nim,cari)

#6. Binary NIM Search
def pencbin(nim,cari):
    awal=1
    akhir=len(nim)+1
    ketemu=False
    iter=0
    while (awal<=akhir) and not ketemu:
        iter+=1
        tengah=int((awal+akhir)/2)
        if cari==nim[tengah]:
            ketemu=True
            print('Angka',cari,'Ditemukan di posisi:',tengah)
        elif(cari<nim[tengah]):
            akhir=tengah-1
        else:
            awal=tengah+1
    if ketemu==False:
        print('Angka tidak ditemukan')
    print('Jumlah Iterasi:',iter)

nim=[2,0,0,0,0,1,6,0,1,5]
nim.sort()
print('List Data', nim)
cari=0
pencbin(nim,cari)

#7. Binary search "sistem informasi"
def pencbin(hur,cari):
    awal=1
    akhir=len(hur)+1
    ketemu=False
    iter=0
    while (awal<=akhir) and not ketemu:
        iter+=1
        tengah=int((awal+akhir)/2)
        if cari==hur[tengah]:
            ketemu=True
            print('Huruf',cari,'Ditemukan di posisi:',tengah)
        elif(cari<hur[tengah]):
            akhir=tengah-1
        else:
            awal=tengah+1
    if ketemu==False:
        print('Huruf tidak ditemukan')
    print('Jumlah Iterasi:',iter)
    
inp_hur="sistem informasi"
print('data awal:',inp_hur)
hur=''.join(sorted(inp_hur))
print('data urut:',hur)
cari='i'
pencbin(hur,cari)

#8. Sequential search "sistem informasi"
def pencseq(hur,cari):
    sis=[]
    for i in range(len(hur)):
        if hur[i]==cari:
            sis.append(i+1)
    print('\nJumlah Iterasi:',i+1)
    if len(sis)>0:
        print('Data:',cari,'\nJumlah %s:'%(cari),len(sis),'\nPosisi data:',sis)
    else:
        print('Data tidak ditemukan')
    return sis

hur='sistem informasi'
print('Data: ', hur)
cari='i'
pencseq(hur,cari)

#9. Binary search Nama
def pencbin(hur,cari):
    awal=1
    akhir=len(hur)+1
    ketemu=False
    iter=0
    while (awal<=akhir) and not ketemu:
        iter+=1
        tengah=int((awal+akhir)/2)
        if cari==hur[tengah]:
            ketemu=True
            print('Huruf',cari,'Ditemukan di posisi:',tengah)
        elif(cari<hur[tengah]):
            akhir=tengah-1
        else:
            awal=tengah+1
    if ketemu==False:
        print('Huruf tidak ditemukan')
    print('Jumlah Iterasi:',iter)
    
inp_hur="teguh dwi cahya kusuma"
print('data awal:',inp_hur)
hur=''.join(sorted(inp_hur))
print('data urut:',hur)
cari='a'
pencbin(hur,cari)

#10.Sequential search Nama
def pencseq(hur,cari):
    sis=[]
    for i in range(len(hur)):
        if hur[i]==cari:
            sis.append(i+1)
    print('\nJumlah Iterasi:',i+1)
    if len(sis)>0:
        print('Data:',cari,'\nJumlah %s:'%(cari),len(sis),'\nPosisi data:',sis)
    else:
        print('Data tidak ditemukan')
    return sis

hur='teguh dwi cahya kusuma'
print('Data: ', hur)
cari='a'
pencseq(hur,cari)

