#VAriabel Global
x='Ini variabel Global'
print(x)

#Var Lokal
def var():
    x='Ini variabel Lokal'
    return x
var()

#Memanggil var Global
x='Ini variabel Global '
def asem():
    global x
    x*=3
    print(x)
asem()

#Tanpa Variabel Nonlokal
def luar():
    x="Sedihnya sampe to the bone :')"
    def dalam():
        x='Seneng lah kan'
        print('Sering Chatan,', x)
    dalam()
    print('Eh Friendzone,',x)
luar()

#Dengan Variabel nonlocal
def Teguh():
    x='mo nembak'
    def dalam():
        nonlocal x
        x='udah friedzone duluan'
        print('sering chatan', x)
    dalam()
    print('yaudahlahya',x)
Teguh()


#CRUD Buku
buku=[]
#Fungsi menampilkan data
def liat_buku():
    global buku
    maaf="Maaf, anda belum memasukkan buku apapun"
    if len(buku)<=0:
        print(maaf)
    else:
        print('List buku anda')
        for indek in range(len(buku)):
            print("%i. %s"%(indek+1,buku[indek]))
    return buku

#fungsi Mengimput data
def inp_buku():
    global buku
    bbaru=input('Masukkan nama buku: ')
    buku.insert(len(buku)+1,bbaru)
    return bbaru

#fungsi untuk Mengedit data
def edit_buku():
    global buku
    if len(buku)<=0:
        print('Anda belum membuat list/List anda kosong')
    else:
        for indek in range(len(buku)):
            print("%i. %s"%(indek+1,buku[indek]))
        edt=int(input("Masukkan indeks buku yang ingin diedit: "))
        if edt>len(buku) or edt<=0:
            print('Mohon masukkan Indek buku yang sesuai, progam akan kembali ke pilihan...')
        else:
            nam=input('Masukkan judul  yang baru: ')
            buku[edt-1]=nam
            return edt

#fungsi untuk menghapus data
def hps_buku():
    global buku
    print('List buku anda')
    if len(buku)<=0:
        print('Anda belum membuat list/List anda kosong')
    else:
        for indek in range(len(buku)):
            print("%i. %s"%(indek+1,buku[indek]))
        hps=int(input("Masukkan indeks buku yang ingin dihapus: "))
        if hps>len(buku) or hps<=0:
            print('Mohon masukkan Indek buku yang sesuai, progam akan kembali ke pilihan...')
        else:
            del buku[hps-1]
        return hps

while True:
    print('''
List Perintah CRUD + Perintah tambahan:
    1 => Melihat buku
    2 => Memasukkan buku
    3 => Mengedit buku
    4 => Menghapus buku
Tekan sembarang untuk keluar..
          ''')
    pil=input("Masukkan pilihan anda: ")
    if pil=='1':
        liat_buku()
    elif pil=='2':
        inp_buku()
    elif pil=='3':
         edit_buku()
    elif pil=='4':
        hps_buku()
    else:
        break


