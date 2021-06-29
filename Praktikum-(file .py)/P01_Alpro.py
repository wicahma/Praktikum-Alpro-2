#Luas Lingkaran
def Lling (r):
    Hsl=3.14*r**2
    if r<=0:
        print("Lingkaran anda Salah")
    else:
        print('Luas Lingkaran Anda',round(Hsl,2))
    return Hsl

#Nilai Minimum
def Nmin ():
    Nilai=[]
    prog='n'
    Ang=()
    print("\nProgram menghitung nilai minimum tanpa batas,\ntekan '00' apabila ingin berhenti \ndan melihat hasil nilai minimum")
    #Memasukkan Angka
    while prog=='n':
        Ang=input('Angka: ')
        if Ang=="00": break
        Nilai.append(Ang)
    Hsl=Nilai[1]
    #Menentukan Nilai Terbesar
    for angka in Nilai:
        if float(angka) < float(Hsl):
            Hsl=angka
    print('List Nilai anda\n',Nilai)
    return Hsl

#Nilai Rata-Rata
def Nrat():
    Nilai=[]
    loop='y'
    print('''Program menghitung nilai rata-rata tanpa batas,\ntekan '00' apabila ingin berhenti \ndan melihat hasil nilai rata-rata ''')
    while loop=='y':
        inp=input('Angka: ')
        if inp=='00': break
        Nilai.append(inp)
    jml=0
    for angka in (Nilai):
        jml+= float(angka)
    Hsl=jml/len(Nilai)
    print('jumlah nilai anda: ',round(jml,2))
    return Hsl

#Program memilih
def pilihan():
    while True:
        print('''
    List pilihan:
        1 => Menghitung Luas Lingkaran
        2 => menghitung Nilai Terkecil
        3 => Menghitung Rata-Rata
    Tekan sembarang untuk keluar...
              ''')
        pil=input("Masukkan pilihan anda: ")
        if pil=='1':
            r=float(input('Masukkan Jari-jari: '))
            Lling(r)
        elif pil=='2':
            print('Nilai terkecil anda',Nmin())
        elif pil=='3':
            print('Nilai rata rata anda',round(Nrat(),2))
        else:
            break
    return pil

print(pilihan(),'\nProgram selesai...')   