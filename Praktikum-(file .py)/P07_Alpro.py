# Faktorial ( ! )
def faktorial(n):
    if n==0:
        return 1
    else:
        return n*faktorial(n-1)
print(faktorial(3))

# Fibonacci 
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(int(input('Angka: '))))

#1. Program Fibonacci menggunakan for/while
#variabel Global
fibo=[0]
#Fungsi Def
def fibb(inp):
    ank1=1
    ank2=0
    a=0
    for x in range(inp):
        a=ank1+ank2
        ank1=ank2
        ank2=a
        fibo.append(a)
        
    return a

#Input & Fungsi pemanggil
while True:
    print('\n==Program Fibonacci')
    inp=int(input('Input Bilangan: '))
    if inp >=0:
        print('\nBilangan Fibonacci ke-%i dari input diatas adalah %i'%(inp,fibb(inp)),'\nDeret Fibonacci \n    ',fibo)
        del fibo[1:len(fibo)]
    else:
        print('Mohon masukkan angka, hanya bilangan cacah')
    print('\n==Enter untuk lanjut, s untuk berenti')
    loop=input('Continue... ')
    if loop=='s':
        break
    else:
        True
print('Program selesai..')


#2. Program fungsi 2^x
#fungsi 2^x
#Fungsi def untuk membuat fungsi rekursinya
def pan(inp):
    #==Kasus Penyetop (Stoop case)
    #            Fungsi if untuk memberikan penbatas dari perulangan, 
    #       agar fungsi rekursi dapat berhenti apabila 
    #       kondisi yang diinginkan telah terpenuhi
    if inp==0:
        return 1
    #==Kasus Rekursi (Recursion Case)
    #            Fungsi else merupakan fungsi utama rekursi
    #       pada fungsi ini terjadi sebuah pengulangan def 
    #       yang masuk kedalam def, jadi apabila fungsi if diatas
    #       telah benar benar terpenuhi, maka rekursi akan berhenti
    #       dan output akan diberikan, sebagai hasil dari perulangan
    else:
        return 2*pan(inp-1)
pan(2)
#             Fungsi Rekursi ini mirip seperti perulangan for dan while,
#       hanya saja fungsi ini lebih sulit, dan juga sering menimbulkan error
#       apabila tidak dibuat dengan hati hati

#fungsi Rekursi 2^x
def pan(inp):
    if inp==0:
        return 1
    else:
        return 2*pan(inp-1)

#Perulangan While
while True:
    print('\n==Program 2^x')
    inp=int(input('Pangkat -->'))
    if inp >=0:
        print('Hasil dari 2 pangkat %i adalah: %i'%(inp,pan(inp)))
    else:
        print('Mohon masukkan angka, hanya bilangan cacah')
    print('\n==Enter untuk lanjut, s untuk berenti')
    loop=input('Continue... ')
    if loop=='s':
        break
    else:
        True
        
print('Program selesai..')

#fungsi def
def pen(inp):
    a=2
    for i in range(inp-1):
        a=a*2
    return a

#Fungsi Pemanggil
while True:
    print('\n==Program 2^x')
    inp=int(input('Pangkat -->'))
    if inp >=0:
        print('Hasil dari 2 pangkat %i adalah: %i'%(inp,pen(inp)))
    else:
        print('Mohon masukkan angka, hanya bilangan cacah')
    print('\n==Enter untuk lanjut, s untuk berenti')
    loop=input('Continue... ')
    if loop=='s':
        break
    else:
        True

print('Program selesai..')


