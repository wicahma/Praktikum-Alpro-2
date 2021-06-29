#1. Insertion Sort Descending
#Fungsi def Descending
def insertionSort(List):
    for index in range(1,len(List)):
        Kanan = List[index]
        Kiri = index - 1
        while Kiri >=0 and List[Kiri] < Kanan:
                List[Kiri + 1] = List[Kiri]
                Kiri -= 1
        List[Kiri+1] = Kanan
    return(List)

#Input Perulangan
def loops():
    while True:
        inp=str(input('Masukkan angka: '))
        if inp=='00':
            break
        else:
            List.append(float(inp))
    return(inp)

List=[]
loops()
print('List Awal:',List)
print()
print('Hasil Akhir:',insertionSort(List))

#2. Insertion Sort Descending (Dengan Penjelasan)
#Fungsi def Descending
def insertionSort(List):
    for index in range(1,len(List)):
        Kanan = List[index]
        Kiri = index - 1
        gsr=0
        print('Iterasi ke',index)
        while Kiri >=0 and List[Kiri] < Kanan:
                List[Kiri + 1] = List[Kiri]
                Kiri -= 1
                gsr+=1
                print('Pergeseran Ke',gsr,',List: ',List)
        List[Kiri+1] = Kanan
        print('List',List)
        print()
    return(List)

#Input Perulangan
def loops():
    while True:
        inp=str(input('Masukkan angka: '))
        if inp=='00':
            break
        else:
            List.append(float(inp))
    return(inp)

List=[]
loops()
print('List Awal:',List)
print()
print('Hasil Akhir:',insertionSort(List))

