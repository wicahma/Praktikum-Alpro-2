#Variabel Global
urutan=[]
A='c'
#Fungsi Pengurutan Insertion Sort Ascending
def insertion_sort():
    for A in range(len(urutan)-1):
        nil_min=A
        for B in range(A+1,len(urutan)):
            if urutan[nil_min]>urutan[B]:
                nil_min=B
        temp=urutan[A]
        urutan[A]=urutan[nil_min]
        urutan[nil_min]=temp
    return(urutan)

#Fungsi untuk input
def inp():
    while True:
        inp_urut=(input("Angka anda: "))
        if inp_urut=='00':
            break
        else:
            urutan.append(float(inp_urut))
    return inp_urut
          
while A=='c':
    print("Tekan '00' untuk berhenti")
    inp()
    insertion_sort()
    print('\nHasil Pengurutan secara Ascending: ',urutan)
    del urutan[0:len(urutan)+1]
    A=input('Tekan c untuk lanjut, sembarang untuk selesai...\n:' )
print('program selesai...')

#Variabel Global
urutan=[]
#Fungsi Pengurutan Insertion Sort Descending
def insertion_sort():
    global urutan
    for A in range(len(urutan)-1):
        nil_min=A
        for B in range(A+1,len(urutan)):
            if urutan[nil_min]<urutan[B]:
                nil_min=B
        temp=urutan[A]
        urutan[A]=urutan[nil_min]
        urutan[nil_min]=temp
        print('Iterasi ke ',A,urutan)
    return(urutan)

#Fungsi untuk input
def inp():
    while True:
        inp_urut=(input("Angka anda: "))
        if inp_urut=='00':
            break
        else:
            urutan.append(float(inp_urut))
    return inp_urut
         
A='c'
while A=='c':
    print("Tekan '00' untuk berhenti\nMasukkan angka anda")
    inp()
    print('\nPengurutan:')    
    insertion_sort()
    print('\nHasil Pengurutan secara Descending: ',urutan)
    del urutan[0:len(urutan)+1]
    A=input('Tekan c untuk lanjut, sembarang untuk selesai...\n:' )
print('program selesai...')



#Variabel Global
urutan=[4,3,5,6,2,78,98]
#Fungsi Pengurutan Insertion Sort Descending
def insertion_sort():
    global urutan
    for A in range(len(urutan)):
        nil_min=A
        for B in range(A+1,len(urutan)):
            if urutan[nil_min]<urutan[B]:
                nil_min=B
        print('indek key:',A,'Tukar :',nil_min)
        temp=urutan[A]
        urutan[A]=urutan[nil_min]
        urutan[nil_min]=temp
        print('Iterasi ke ',A,urutan)
        print()
    return(urutan)

#Fungsi untuk input
def inp():
    while True:
        inp_urut=(input("Angka anda: "))
        if inp_urut=='00':
            break
        else:
            urutan.append(float(inp_urut))
    return inp_urut

A='c'
while A=='c':
    print("Tekan '00' untuk berhenti\Masukkan angka anda")
    inp()
    print('\nPengurutan:')    
    insertion_sort()
    print('\nHasil Pengurutan secara Descending: ',urutan)
    del urutan[0:len(urutan)+1]
    A=input('Tekan c untuk lanjut, sembarang untuk selesai...\n:' )
print('program selesai...')