class mahasiswa():
    jumlah=0
    def __init__(mhs,nama,prodi,NIM):
        mhs.prod=prodi
        mhs.nam=nama
        mhs.nim=NIM
        mhs.prod=prodi
        mahasiswa.jumlah+=1
    def tampil_jumlah(mhs):
        print("jumlah mahasiswa %d: ", mahasiswa.jumlah)
    def tampil_mahasiswa(mhs):
        print('nama: ',mhs.nam,'NIM: ',mhs.nim,'Prodi: ',mhs.prod)

mhs1=mahasiswa('udin','Teknik Mikrobiologi',2000016015)
mhs2=mahasiswa("rehan","Bahasa Meme",160016002)
mhs3=mahasiswa("tina","bahasa India",140016003)
mhs4=mahasiswa("desi","Sasta Arab",130016004)
mhs1.tampil_mahasiswa()
mhs2.tampil_mahasiswa()
mhs3.tampil_mahasiswa()
mhs4.tampil_mahasiswa()
mahasiswa.jumlah

#Tugas
class kendaraan_darat():
    leng=''
    jml=0
    print('''==Keterangan

    >>Jenis kendaraan
        1. Mobil
        2. Motor
        3. Lainnya

    >>Jenis Plat
        1. Hitam
        2. Kuning
        3. Merah
        4. Putih
        5. Hijau
    >>Kelengkapan
        Tekan y untuk ada, n untuk tidak ada
    ''')
    def __init__(self,merk,milik,plat):
        self.merk=merk
        self.milik=milik
        self.plat=plat
    def _hit(self):
        jns=['Mobil','Motor','Lainnya']
        jn_plat=['Hitam','Kuning','Merah','Putih','Hijau']
        self.pajak=int(input('Tahun Pajak=> '))
        self.jenis=jns[int(input('Jenis Kendaraan=> '))-1]
        self.j_plat=jn_plat[int(input('Jenis Plat=>'))-1]
    def _surr(self):
        self.leng+=input('Kelengkapan BPKB=> ')
        self.leng+=input('Kelengkapan STNK=> ')
    def _data(self):
        kendaraan_darat.jml+=1
        print('\n==Data %i \nMerek: %s \nPemilik: %s \nPlat: %s' %(kendaraan_darat.jml,self.merk,self.milik,self.plat),end=' ')
        kendaraan_darat._hit(self)
        kendaraan_darat._surr(self)

        if self.leng=='yy':
            s='Surat lengkap'
        else:
            s='Surat tidak lengkap'
        if self.pajak+5 < 2021:
            p='Belum Lunas Pajak'
        else:
            p='Lunas Pajak'
        print('(Plat %s) \nJenis: %s \nSurat surat: %s \nPajak: (%i) %s'%(self.j_plat,self.jenis,s,self.pajak+5,p))

kend=kendaraan_darat('Honda','Udin','KB 2112 JK')
kend2=kendaraan_darat('Suzuki','Nurrahman','B 6271 CA')
kend._data()
kend2._data()


